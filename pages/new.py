import streamlit as st
# from sqlite3 import Error
import database_control
import pandas as pd

def app():
    # st.markdown("""
    # <style>
    #     section[data-testid="stSidebar"][aria-expanded="true"]{
    #         display: none;
    #     }
    # </style>
    # """, unsafe_allow_html=True)

    cnx = database_control.create_connection()
    df = pd.read_sql_query("SELECT * FROM tech_support", cnx)    

    doc_types = database_control.doc_type_get_all(cnx)
    popover_insert = st.popover("Add New", use_container_width=True)  

    # with popover_insert.form("New Entry", clear_on_submit=True):       
    with st.form("Create New", clear_on_submit=True):
        #res = database_control.doc_type_get_all(cnx)
        #print("GET ALL DOC_TYPE: ",  res)
        #date_created = st.date_input("Date Created")
        title =popover_insert.text_input("Title: ")
        doc_type = popover_insert.selectbox("Select one ", doc_types.title)
        category = popover_insert.text_input("Category: ")
        symptom = popover_insert.text_area("Symptom: ")
        resolution = popover_insert.text_area("Resolution: ")

        submit_new = popover_insert.form_submit_button('Submit')

        if submit_new:
            print("Title to save ", title)
            database_control.add_row(cnx, title, doc_type, category, symptom, resolution)
            st.success('Updated OK') 
#           st.rerun()