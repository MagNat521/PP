import psycopg2
from psycopg2 import pool

# Инициализация пула соединений (лучше вынести параметры в конфиг)
postgresql_pool = None

def init_db_pool():
    global postgresql_pool
    postgresql_pool = psycopg2.pool.SimpleConnectionPool(
        1, 10,
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port",
        database="your_database"
    )

def get_connection():
    if postgresql_pool is None:
        init_db_pool()
    return postgresql_pool.getconn()

def release_connection(conn):
    postgresql_pool.putconn(conn)

def close_all_connections():
    postgresql_pool.closeall()