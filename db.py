import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)

def db_connection():
    
    if conn:
        print('DB connection successful')
        return True
    else:
        print('DB connection failed')
        return False