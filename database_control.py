import streamlit as st
import sqlite3
from sqlite3 import Error
#-----------------------------
# Source: https://drive.google.com/drive/folders/1exzHognJY59XdaSSHZzXuPARFdLyf7s0

path =  './'
db_name = 'ush_2.db'

def create_connection():
    conn = None
    try:
        #conn = sqlite3.connect(path+db_name)
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)
    return conn

# CREATE NEW DB AND TABLES -------------------------
def create_table(conn):
    try:
        c = conn.cursor()
        #c.execute('''CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, date text NOT NULL, amount numeric(5,2) NOT NULL, payee text NOT NULL, category text, account text, note text)''')
        c.execute('''CREATE TABLE IF NOT EXISTS tech_support (                  
                  id INTEGER PRIMARY KEY,        
                  date_created DATETIME DEFAULT CURRENT_TIMESTAMP,
                  title TEXT NOT NULL,
                  category TEXT,
                  symptom TEXT,
                  resolution TEXT,
                  rating INTEGER)''')
        conn.commit()
    except Error as e:
        print(e)

def create_db_and_tables():
    conn = create_connection()
    create_table(conn)
# END OF CREATE NEW DB AND TABLES -------------------
    
    # INSERT DUMMY DATA ---------------------------------
    # c = conn.cursor()
    # c.execute("INSERT INTO tech_support (title, category, symptom, resolution) VALUES (?, ?, ?, ?)", (title, category, symptom, resolution))
    # conn.commit()

# INSERT SINGLE ROW ---------------------------------
def add_row(conn, title, category, symptom, resolution):
    try:
        print("Passed In to Add: ", title)
        c = conn.cursor()
        c.execute("INSERT INTO tech_support (title, category, symptom, resolution) VALUES (?, ?, ?, ?)", (title, category, symptom, resolution))
        conn.commit()
    except Error as e:
        print("Error: ", e)

# Delete Row:
def delete_row(conn, ids):
    #print("IDS to delete: ", ids)
    for id in ids:
        print("Deleted Id: ", id)


    try:
        c = conn.cursor()
        for id in ids:
            c.execute("DELETE FROM tech_support WHERE id=?", (id,))
            conn.commit()
        #st.info("OK. Successfuly deleted!")
        #st.popover("OK. Successfuly deleted!")
        st.rerun()
    except Error as e:
        print(e)    