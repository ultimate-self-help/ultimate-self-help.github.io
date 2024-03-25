import streamlit as st
import sqlite3
from sqlite3 import Error
import pandas as pd
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
        # Main tech_support table. Create.
        #c.execute('''CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, date text NOT NULL, amount numeric(5,2) NOT NULL, payee text NOT NULL, category text, account text, note text)''')    
        c.execute('''CREATE TABLE IF NOT EXISTS tech_support (                  
                  id INTEGER PRIMARY KEY AUTOINCREMENT,        
                  date_created DATETIME DEFAULT CURRENT_TIMESTAMP,
                  title TEXT NOT NULL,
                  doc_type TEXT NOT NULL REFERENCES doc_type(id),
                  category TEXT NOT NULL REFERENCES category(id),
                  symptom TEXT,
                  resolution TEXT,
                  rating INTEGER)''')
        conn.commit()

        # Category Table. Create.
        c.execute('''CREATE TABLE IF NOT EXISTS category (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT)''')
        conn.commit()
        print("2 Tables created OK.")

        # DOC_TYPE LOOKUP TABLE. WORKS BUT RELATIONSHIP WRONG DIRECTION.
        # c.execute('''CREATE TABLE IF NOT EXISTS doc_type (
        #           id INTEGER PRIMARY KEY AUTOINCREMENT,
        #           title TEXT NOT NULL,
        #           tech_support_id INTEGER NOT NULL REFERENCES tech_support(id))''')
        # conn.commit()
        # print("2 Tables created OK.")


        # doc_type table. Create.
        c.execute('''CREATE TABLE IF NOT EXISTS doc_type (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL)''')
        conn.commit()
        print("2 Tables created OK.")

        
        # Set inital data.
        c.execute("INSERT INTO doc_type (title) VALUES ('Work Instructions')")
        c.execute("INSERT INTO doc_type (title) VALUES ('Incident')")
        c.execute("INSERT INTO doc_type (title) VALUES ('Request')")
        conn.commit()
    except Error as e:
        print(e)
    conn.close()


def create_db_and_tables():
    conn = create_connection()
    create_table(conn)
    conn.close()


# Database. Insert. Single row.
def add_row(conn, title, doc_type, category, symptom, resolution):
    try:
        print("Passed In to Add: ", title)
        c = conn.cursor()
        c.execute("INSERT INTO tech_support (title, doc_type, category, symptom, resolution) VALUES (?, ?, ?, ?, ?)", (title, doc_type, category, symptom, resolution))
        conn.commit()
    except Error as e:
        print("Error: ", e)
    conn.close()

def update_single_row(conn, data ):
    # id = data.id
    # title = data.title
    # doc_type = data.doc_type
    # category = data.category

    # WORKING FOR VALUES. NO ID.
    # for row in data["edited_rows"].values():
    #     print("ROW: ", row['title'])

    d =  data["edited_rows"].items()
    for key, value in d:
        print("DB Id: ", key) # 0
        print("VALUE: ", value) # {'title:'222'}
        for key, value in value.items():
             print("v2: ", key) # 'title
             print("v2: ", value) # '222'

        #c = conn.cursor()
        # # c.execute(f"UPDATE tech_support SET id={id}, title={title}, doc_type={doc_type}, category={category}")
        # #c.executemany("UPDATE tech_support SET title = ? doc_type = ? category = ? WHERE id = ?", (title, doc_type, category, id))
        # c.execute("""UPDATE tech_support SET title = ?, doc_type = ?, category = ? WHERE id = ?""", (title, doc_type, category, id))
        # c.execute("""UPDATE tech_support SET title = ?, doc_type = ?, category = ? WHERE id = ?""", (value, key))
        # conn.commit()   

# Delete. Single Row.
def delete_row(conn, ids):
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
    conn.close()


# doc_type
def doc_type_get_all(conn):
    try:
        print("IN...")
        c = conn.cursor()
        df2 = pd.read_sql_query("SELECT * FROM doc_type", conn)
        #print("RESPT :", df2 )
        #optionslist = list(df2)
        return df2
    
    except:
        pass
    conn.close()



