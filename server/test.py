import logging, sys
from managers.accountmanager import AccountManager

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
sh_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(sh_handler)

print AccountManager.add_new_account({'user': 'loming2', 'email': 'loming2@loming.com', 'password': 'test'})