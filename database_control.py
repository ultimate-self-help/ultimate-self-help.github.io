import sqlite3
import streamlit as st
# def create_database():
#     # conn = sqlite3.connect('database.db')
#     # c = conn.cursor()
#     # c.execute("""
#     #           SELECT income
#     #         """)
#     # c.execute("""CREATE TABLE finances (date Date, income )""")
#     pass

# def insert_period(period, incomes, expenses, comment):
#     pass
#-----------------------------
# Source: https://drive.google.com/drive/folders/1exzHognJY59XdaSSHZzXuPARFdLyf7s0

#path =  './'
db_name = 'ush_1.db'

def create_connection():
    conn = None
    try:
        #conn = sqlite3.connect(path+db_name)
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)
    return conn

### Income  ####
# def create_table(conn):
#     try:
#         c = conn.cursor()
#         c.execute('''CREATE TABLE IF NOT EXISTS title (id INTEGER PRIMARY KEY, date text NOT NULL, amount numeric(5,2) NOT NULL, payee text NOT NULL, category text, account text, note text)''')
#         c.execute('''CREATE TABLE IF NOT EXISTS payee (id INTEGER PRIMARY KEY,name text NOT NULL)''')
#         c.execute('''CREATE TABLE IF NOT EXISTS category (id INTEGER PRIMARY KEY,name text NOT NULL)''')
#         c.execute('''CREATE TABLE IF NOT EXISTS account (id INTEGER PRIMARY KEY,name text NOT NULL)''')

#         conn.commit()
#     except Error as e:
#         print(e)

# def create_db_and_tables():
#     conn = create_connection()
#     create_table(conn)

def get_items_all():
    conn = create_connection()
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM items")
        rows = c.fetchall()
        names = [row[0] for row in rows]
        return names
    except Error as e:
        print(e)