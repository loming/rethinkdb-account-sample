from common.database import Database, dbwrapper
from common.singleton import Singleton
import traceback
import rethinkdb as r
import logging
import hashlib, uuid
from datetime import datetime
from tzlocal import get_localzone

logger = logging.getLogger()

class AccountManager(Singleton):
    ##TODO change to session token
    @staticmethod
    @dbwrapper(action='auto login')
    def auto_login(user, hashed_password, conn=None):
        cursor = r.table('accounts').filter({'user': user}).run(conn)

        if len(cursor.items) == 0:
            logger.info("User not found '{0}'".format(user))
            return None

        doc = cursor.next()
        if doc.password == hashed_password:
            return doc
        else:
            logger.info("User '{0}' found but pass doesn't match".format(user))
            return None

    @staticmethod
    @dbwrapper(action='manual login')
    def manual_login(user, password, conn=None):
        cursor = r.table('accounts')\
            .filter({'user': user})\
            .limit(1)\
            .run(conn)

        if len(cursor.items):
            doc = cursor.next()
            if AccountManager._validate_password(password, doc['salt'], doc['password']):
                return doc
            else:
                return 'invalid-password'
        else:
            logger.info("manualLogin: User not found {0}".format(user))
            return 'user-not-found'


    ## CRUD operations: record insertion, update & deletion methods

    ##
    # Create a new account using [`insert`]
    # @param {Object} newData
    ##
    @staticmethod
    @dbwrapper(action='add new account')
    def add_new_account(new_data, conn=None):
        cursor = r.table('accounts')\
            .filter(r.or_(r.row['user'].eq(new_data['user']), r.row['email'].eq(new_data['email'])))\
            .limit(1)\
            .run(conn)

        if len(cursor.items):
            doc = cursor.next()
            if doc['user'] == new_data['user']:
                return 'username-taken'
            else:
                return 'email-taken'
        else:
            new_data['salt'], new_data['password'] = AccountManager._salt_and_hash_password(new_data['password'])
            new_data['createDate'] = datetime.now(tz=get_localzone())

            result = r.table('accounts').insert(new_data).run(conn)

            if result and result['inserted'] == 1:
                new_data['id'] = result['generated_keys'][0]
                return new_data
            else:
                logger.error('[add new account][insert_failed]: {0}'.format(result))
                return None

    @staticmethod
    def update_account(new_data):
        # if user didn't change password
        if 'password' in new_data and new_data['password'] == '':
            new_data.pop('password')
        elif 'password' in new_data:
            new_data['salt'], new_data['password'] = AccountManager._salt_and_hash_password(new_data['password'])

        return AccountManager._update(new_data)

    @staticmethod
    @dbwrapper(action='update account')
    def _update(new_data, conn=None):
        result = r.table('accounts')\
            .filter({'user': new_data['user']})\
            .limit(1)\
            .update(new_data)\
            .run(conn)

        if result['replaced'] == 1:
            return new_data
        else:
            logger.error('[update account][replace_failed]: {0}'.format(result))
            return None

    ##
    # Update the password retrieving firstly the account by the given `email`
    # using [`filter`] and than [`update`].
    # @param {String} email
    #   the email of the account
    # @param {String} newPass
    #    the new password (non-hashed yet)
    ##
    @staticmethod
    @dbwrapper(action='update password')
    def update_password(email, new_password, conn=None):
        salt, hashed_password = AccountManager._salt_and_hash_password(new_password)

        result = r.table('accounts')\
            .filter({email: email})\
            .limit(1)\
            .update({'salt':salt, 'password': hashed_password})\
            .run(conn)

        if result['replaced'] == 1:
            return True
        else:
            logger.error('[update password][replace_failed]: {0}'.format(result))
            return None

    @staticmethod
    def _salt_and_hash_password(password):
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(password + salt).hexdigest()

        return salt, hashed_password

    @staticmethod
    def _validate_password(password, salt, hashed_password):
        if hashed_password == hashlib.sha512(password + salt).hexdigest():
            return True
        else:
            return False

    ## account lookup methods

    ##
    # Retrieve an account given the `email` using [`filter`].
    # @param {String} email
    #    the account email
    ##
    @staticmethod
    @dbwrapper(action='get account by email')
    def get_account_by_email(email, conn=None):

        cursor = r.table('accounts')\
            .filter({'email': email})\
            .limit(1)\
            .run(conn)

        if len(cursor.items):
            doc = cursor.next()
            return doc
        else:
            logger.error('[get account by email][retrieve failed]: {0}'.format(email))
            return None

    ##
    # Validate a reset password link by finding the account
    # associated with the `email` and reset code using
    # [`filter`] with an [`and`] condition.
    # @param {String} email
    #    the account email
    # @param {String} reset_code
    #    the account reset code
    ##
    @staticmethod
    @dbwrapper(action='validate reset code')
    def validate_reset_code(email, reset_code, conn=None):
        cursor = r.table('account_reset_codes')\
            .filter({'email': email, 'reset_code': reset_code})\
            .limit(1)\
            .run(conn)

        if len(cursor.items):
            logger.info("[validate reset code][success]: {0}".format(email))
            return 'ok'
        else:
            logger.info("[validate reset code][failure]: {0}, {1}".format(email, reset_code))
            return None

    ##
    # Retrieve all accounts using [`table`]
    ##
    @staticmethod
    @dbwrapper(action='get all accounts')
    def get_all_accounts(conn=None):
        cursor = r.table('accounts')\
            .run(conn)

        return list(cursor)

    ##
    # Delete an account by `id` using [`get`] followed by [`del`].
    # @param {String} id
    #    the account id
    ##
    @staticmethod
    @dbwrapper(action='delete account')
    def delete_account(acc_id, conn=None):
        result = r.table('accounts')\
            .get(acc_id)\
            .delete()\
            .run(conn)

        if result['deleted'] == 1:
            return True
        else:
            return False
