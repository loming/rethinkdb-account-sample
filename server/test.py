import logging, sys
from managers.accountmanager import AccountManager

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
sh_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(sh_handler)

logger.info('Create Account:-\n{0}\n'.format(
    AccountManager.add_new_account({'user': 'loming', 'email': 'loming@loming.com', 'password': 'test'})
))

user = AccountManager.manual_login('loming', 'test')
logger.info('Login:-\n{0}\n'.format(
    user
))

logger.info('Login:-\n{0}\n'.format(
    AccountManager.manual_login('loming', 'test2')
))

user.update({'password': 'test'})
logger.info('Update account with password:-\n{0}\n'.format(
    AccountManager.update_account(user)
))

user.pop('password')
logger.info('Update account without password:-\n{0}\n'.format(
    AccountManager.update_account(user)
))

logger.info('Get account by email:-\n{0}\n'.format(
    AccountManager.get_account_by_email('loming@loming.com')
))

logger.info('Get account by email:-\n{0}\n'.format(
    AccountManager.get_account_by_email('loming2@loming.com')
))

logger.info('Get all accounts:-\n{0}\n'.format(
    AccountManager.get_all_accounts()
))

logger.info('Delete account {0}:-\n{1}\n'.format(
    user['id'],
    AccountManager.delete_account(user['id'])
))

