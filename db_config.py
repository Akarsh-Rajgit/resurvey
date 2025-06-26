import pymysql
from flask import g

def get_db_connection():
    if 'db' not in g:
        g.db = pymysql.connect(
            host="localhost",
            user="root",
            password="Ichigo_bankai24",
            database="resurvey",
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db

def close_db_connection(error=None):
    db = g.pop('db', None)
    if db is not None:
        try:
            if db.open:
                db.close()
        except Exception as e:
            pass  
