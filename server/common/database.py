import logging
import ConfigParser
from rethinkpool import *
from rethinkdb.errors import RqlRuntimeError
from singleton import Singleton
import traceback
import time

# Setup the configuration
dbConfig = ConfigParser.ConfigParser()
dbConfig.read('dbConfig.conf')

# Setup the logger
logger = logging.getLogger()

# configure connection pooling if settings are provided in `dbConfig`
name = 'rethinkdb'
host = dbConfig.get('Pool', 'Host')
port = dbConfig.get('Pool', 'Port')
db = dbConfig.get('Pool', 'DB')
max = int(dbConfig.get('Pool', 'Max')) or 1000
min = int(dbConfig.get('Pool', 'Min')) or 2
log = bool(dbConfig.get('Pool', 'Log')) or True
idleTimeoutMillis = float(dbConfig.get('Pool', 'idleTimeoutMillis')) or 1 * 60 * 1000
reapIntervalMillis = float(dbConfig.get('Pool', 'reapIntervalMillis')) or 30 * 1000

def dbSetup():
    connection = r.connect(host=host, port=port)
    try:
        r.db_create(db).run(connection)
        r.db(db).table_create('accounts').run(connection)
        r.db(db).table_create('account_reset_codes').run(connection)
        print 'Database setup completed'
    except RqlRuntimeError:
        print 'Database already exists.'
    finally:
        connection.close()
dbSetup()

class Database(Singleton):
    def __init__(self):
        self.connectionPool = RethinkPool(max_conns=max,
                                          initial_conns=min,
                                          host=host,
                                          port=port,
                                          db=db,
                                          timeout=idleTimeoutMillis)

    def onConnection(self):
        return self.connectionPool.get_resource()


def dbwrapper(action, benchmark=True):
    def func_decorator(func):
        def func_wrapper(*args,**kwargs):
            start = time.time()
            if benchmark:
                logger.info('[i] started @ {0}, {1}'.format(start, action))

            with Database().onConnection() as res:
                try:
                    result = func(conn=res.conn, *args, **kwargs)
                except:
                    logger.error("[{0}]: {1}".format(action, traceback.format_exc()))
                    result = None

            end = time.time()
            total = 1000 * (end-start)
            if benchmark:
                logger.info('[i] completed in {0}ms'.format(round(total, 2)))
            return result
        return func_wrapper

    return func_decorator

# def pool(ctor, limit=10):
#     local_pool = multiprocessing.Queue()
#     n = multiprocessing.Value('i', 0)
#     @contextlib.contextmanager
#     def pooled(ctor=ctor, lpool=local_pool, n=n):
#         # block iff at limit
#         try: i = lpool.get(limit and n.value >= limit)
#         except multiprocessing.queues.Empty:
#             n.value += 1
#             i = ctor()
#
#             logger.debug("Pooled object: %s", i.id)
#         yield i
#         lpool.put(i)
#     return pooled

