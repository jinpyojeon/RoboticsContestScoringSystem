# -*- coding: utf-8; -*-

import redis
import registry
from constants import settings
from libraries.my_sql_connection import MySQLConnection
from raven import Client
from libraries.repositories.robots import Robots
from libraries.repositories.runs import Runs
from constants import settings

def load_registry():
    """ Initialize and load the global registry
    """
    r = registry.get_registry()
    if r.is_locked():
        return
    init_mysql(r)
    init_redis(r)
    init_clients(r)
    init_db_objects(r)
    r.lock()


def init_mysql(r):
    r['MY_SQL'] = MySQLConnection(
	user=settings.mysql_user,
	passwd=settigs.mysql_password)


def init_redis(r):
    r['REDIS'] = redis.StrictRedis(
        host=settings.redis_host,
        port=settings.redis_port,
        db=settings.redis_db
    )


def init_clients(r):
    r['SENTRY'] = Client(
        'https://858c1ce455dc43538c50f8ca3b3358ce:93608270372'
        'b4b939737b04a3c816612@app.getsentry.com/60618'
    )


def init_db_objects(r):
    r['ROBOTS'] = Robots
    r['RUNS'] = Runs
