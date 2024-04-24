import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv
load_dotenv()
import os

def connect_db():
    con = psycopg2.connect(dbname=os.getenv('DB_NAME'),
        user = os.getenv('DB_USERNAME'),
        host='172.24.0.2',
        password=os.getenv('POSTGRES_PASSWORD'))
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 
    cursor = con.cursor()
    return cursor

def create_table_books():
    try:
        conn = connect_db()
    except:
        print("I am unable to connect to the database")
    try:
        conn.execute("""CREATE TABLE books 
                     (id serial PRIMARY KEY,
                     nome_autor character varying(100),
                     nome_livro character varying(100))
                     ;""")
    except:
        print("I can't drop our test database!")
    conn.close()

