from db import db_connection, conn
import pandas as pd

if db_connection():
    tables = pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';", conn)
    print(tables)
