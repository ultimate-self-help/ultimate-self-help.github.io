import streamlit as st
import subprocess
import sys
import os
import sqlite3
from sqlite3 import Error
import streamlit as st
import database_control
import pandas as pd
import pygwalker as pyg
#import streamlit.components.v1 as components # Old
from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm # New
import numpy as np
from streamlit_extras.dataframe_explorer import dataframe_explorer


def app():
    st.session_state.show_edit_button = True
    st.session_state.user_selected_row = {}
    st.session_state.user_selected_single = {}
    does_db_and_tables_exist = False

    def update_db_with_selected_rows(selected_rows):
        print("TO UPDATE 1: ", selected_rows)
        print("TO UPDATE 2: ", selected_rows['id'].values)
        #print("TO UPDATE 3: ", selected_rows['selected_rows'])

        st.session_state.user_selected_row = selected_rows
        
        print("SELECTED: ", st.session_state.user_selected_row['title'].values)
        st.session_state.user_selected_single = st.session_state.user_selected_row.values
        print("CLEANED: ", st.session_state.user_selected_single)

        if len(selected_rows) > 0:
            st.session_state.show_edit_button = True


    def dataframe_with_selections(df):
        df_with_selections = df.copy()
        df_with_selections.insert(0, "Select", False)

        edited_df = st.data_editor(
            df_with_selections,
            hide_index=True,
            column_config={"Select": st.column_config.CheckboxColumn(required=True)},
            disabled=df.columns,
        )

        selected_indices = list(np.where(edited_df.Select)[0])
        selected_rows = df[edited_df.Select]
        update_db_with_selected_rows(selected_rows)
        return {"selected_rows_indices": selected_indices, "selected_rows": selected_rows}


    cnx = database_control.create_connection()
    df = pd.read_sql_query("SELECT * FROM tech_support", cnx)            
    st.subheader("Hi")


    doc_types = database_control.doc_type_get_all(cnx)
    popover_insert = st.popover("Add New", use_container_width=True)  
    with popover_insert.form("New Entry"):
        #res = database_control.doc_type_get_all(cnx)
        #print("GET ALL DOC_TYPE: ",  res)
        #date_created = st.date_input("Date Created")
        title =popover_insert.text_input("Title: ")
        doc_type = popover_insert.selectbox("Select one ", doc_types.title)
        category = popover_insert.text_input("Category: ")
        symptom = popover_insert.text_area("Symptom: ")
        resolution = popover_insert.text_area("Resolution: ")
        submit = popover_insert.button('Submit')

        if submit:
            print("Title to save ", title)
            database_control.add_row(cnx, title, doc_type, category, symptom, resolution)
            st.success('Updated OK') 
#           st.rerun()
            
    if st.session_state.show_edit_button: 
        update_container = st.container(border=True)                       
        with update_container.form("Update Entry"):
            #res = database_control.doc_type_get_all(cnx)
            #print("GET ALL DOC_TYPE: ",  res)
            #date_created = st.date_input("Date Created")
            print("SELECTED TITLE: ", st.session_state.user_selected_row)
            title = st.text_input("Title: ")
            doc_type = st.selectbox("Select one ", doc_types.title)
            category = st.text_input("Category: ")
            symptom = st.text_area("Symptom: ")
            resolution = st.text_area("Resolution: ")
            submit_update = st.form_submit_button("Update")

            if submit_update:
                print("Title to save ", title)
                # database_control.update_single_row(cnx, title, doc_type, category, symptom, resolution)
                # st.success('Updated OK') 
                # st.rerun()
    
    dataframe_with_selections(df)
    #selection = dataframe_with_selections(df)
    #st.write("Your selection:")
    #st.write(selection)