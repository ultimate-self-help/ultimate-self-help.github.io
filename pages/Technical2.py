import streamlit as st
import database_control
import pandas as pd
#from datetime import datetime
cnx = database_control.create_connection()

# Page Configuration.
st.set_page_config(page_title="Tech DB", layout='wide')


# DISPLAY TABLE ----------------
try:
    cnx = database_control.create_connection()
    df = pd.read_sql_query("SELECT * FROM tech_support", cnx)
    #st.dataframe(df_filtered)
    st.dataframe(df)
except:
    submit = st.button("Create DB (First Time Users)")
    if submit:
        database_control.create_db_and_tables()
    st.write("DB does not exist yet! Create it first!")


#try:
    # title = st.multiselect(
    #     "Select the Merchant:",
    #     options=df["title"].unique(),
    #     default=df["title"].unique(),
    # )

    # df_filtered = df.query(
    #     "title == @title"
    # )
    #st.dataframe(df_filtered)


# if st.button('Add new row / entry.'):
#     title = st.text_input("Title: ")
#     category = st.text_input("Category: ")
#     symptom = st.text_input("Symptom: ")
#     resolution = st.text_input("Resolution: ")
#     database_control.add_row(cnx, title, category, symptom, resolution)
#     st.success('Updated OK')
#     st.rerun()
    

title = st.text_input("Title: ")
category = st.text_input("Category: ")
symptom = st.text_input("Symptom: ")
resolution = st.text_input("Resolution: ")

submit = st.button('Add new row / entry.')

if submit:
    print("TITLE ", title)
    database_control.add_row(cnx, title, category, symptom, resolution)
    st.success('Updated OK')
    st.rerun()
