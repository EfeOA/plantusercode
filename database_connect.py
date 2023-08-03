import mysql.connector
from config import user, PASSWORD, HOST
dbname='plantregister'

def _connect_to_db():
    # Code to connect to a mysql database, uses the auth details
    # in config.py
    connectDB = mysql.connector.connect(
        host=HOST,
        User=user,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=dbname
    )
    return connectDB