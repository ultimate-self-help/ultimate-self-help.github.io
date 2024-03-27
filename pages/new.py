import streamlit as st
# from sqlite3 import Error
import database_control
import pandas as pd


# app():

cnx = database_control.create_connection()
df = pd.read_sql_query("SELECT * FROM tech_support", cnx)    

doc_types = database_control.doc_type_get_all(cnx)
st.subheader("New Entry")
# with popover_insert.form("New Entry", clear_on_submit=True):       
with st.form("Create New", clear_on_submit=True):
    #res = database_control.doc_type_get_all(cnx)
    #print("GET ALL DOC_TYPE: ",  res)
    #date_created = st.date_input("Date Created")
    title = st.text_input("Title: ")
    doc_type = st.selectbox("Select one ", doc_types.title)
    category = st.text_input("Category: ")
    symptom = st.text_area("Symptom: ")
    resolution = st.text_area("Resolution: ")
    link1 = st.text_input("Link 1")
    rating = st.number_input("Rating")

    submit_new = st.form_submit_button('Submit')

    if submit_new:
        print("Title to save ", title)
        database_control.add_row(cnx, title, doc_type, category, symptom, resolution, link1, rating)
        st.success('Updated OK') 
        st.switch_page("main.py")
#           st.rerun()
    
if st.button("Cancel"):
    st.switch_page("main.py")

if st.button("Home"):
    st.switch_page("main.py")