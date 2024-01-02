import sqlite3
import streamlit as st
import database_control
import pandas as pd

st.header("DB test SQLite")

# resp = database_control.get_items_all()
cnx = database_control.create_connection()
df = pd.read_sql_query("SELECT * FROM items", cnx)

# st.write("GET ALL ITEMS: ", df)

title = st.multiselect(
    "Select the Merchant:",
    options=df["title"].unique(),
    default=df["title"].unique(),
)

df_filtered = df.query(
    "title == @title"
)

st.dataframe(df_filtered)