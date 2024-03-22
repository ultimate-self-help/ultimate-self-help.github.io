import subprocess
import sys
import os
import sqlite3
from sqlite3 import Error
import streamlit as st
import database_control
import pandas as pd
from datetime import datetime
from streamlit_option_menu import option_menu 

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

submit = st.button("Create DB (First Time Users)")
if submit:
    database_control.create_db_and_tables()
    
# Source: https://www.youtube.com/watch?v=YClmpnpszq8&list=PL7QI8ORyVSCaejt2LICRQtOTwmPiwKO2n&index=14
if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)


st.dataframe(df_filtered)