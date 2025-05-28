import os
import mysql.connector
from mysql.connector import pooling
from dotenv import load_dotenv

load_dotenv()

dbconfig = {
    "host": os.getenv("DB_HOST", "db"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "secret"),
    "database": os.getenv("DB_NAME", "task_manager"),
    "port": os.getenv("DB_PORT", "3306"),
    "auth_plugin": 'mysql_native_password'  # Для MySQL 8.0+
}

connection_pool = pooling.MySQLConnectionPool(
    pool_name="my_pool",
    pool_size=5,
    **dbconfig
)

def get_connection():
    return connection_pool.get_connection()
