import streamlit as st
import subprocess
import sys
import os
import sqlite3
from sqlite3 import Error
import database_control
import pandas as pd
import pygwalker as pyg
#import streamlit.components.v1 as components # Old
from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm # New
import numpy as np
from streamlit_extras.dataframe_explorer import dataframe_explorer

def app():
    if "show_edit_button" not in st.session_state:
        st.session_state.show_edit_button = False
    
    if "user_selected_title" not in st.session_state:
        st.session_state.user_selected_title = ""

    def dataframe_with_selections(df):
        df_with_selections = df.copy()
        df_with_selections.insert(0, "Select", False)

        edited_df = st.data_editor(
            df_with_selections,
            hide_index=True,
            column_config={"Select": st.column_config.CheckboxColumn(required=True)},
            # on_change=callback_populate_form,
            # args=['user_selected_row']
        )

        selected_indices = list(np.where(edited_df.Select)[0])
        selected_rows_df = df[edited_df.Select]
        print("")
        print("")
        if len(selected_rows_df) > 0:
            print("0. SELECTED ROW: ", selected_rows_df)
            print("1. EDITED_DF: ", selected_rows_df.iloc[0])
            st.session_state.user_selected_row = selected_rows_df.iloc[0]
            print("3 GET DF CELL: ",st.session_state.user_selected_row['title'] )
        else:
            st.session_state.user_selected_row = []
        
        #-------------
        if 'user_selected_row' not in st.session_state:
            st.session_state.user_selected_row = pd.DataFrame()
            
        if len(st.session_state.user_selected_row) > 0:  
            if 'doc_type_key' not in st.session_state:
                st.session_state.doc_type_key = st.session_state.user_selected_row['doc_type']

            doc_type = st.selectbox(
                "Document Type",
                options=doc_types.title,
                 key="doc_type_key"
                )
            
            title = st.text_input(label="Title: ", 
                    value=st.session_state.user_selected_row['title'],
                    on_change=lambda: setattr(
                        st.session_state,
                        'user_selected_row', 
                        st.session_state.key_title
                        ),
                    key='key_title'
                    )
            
            category = st.text_input(label="Category: ", 
                value=st.session_state.user_selected_row['category'],
                on_change=lambda: setattr(
                    st.session_state, 
                    'user_selected_row',
                     st.session_state.key_cat
                    ),
                key='key_cat'
                )
            
            symptom = st.text_input(label="Symptom: ", 
                    value=st.session_state.user_selected_row['symptom'],
                    on_change=lambda: setattr(
                        st.session_state,
                        'user_selected_row', 
                        st.session_state.key_symptom
                        ),
                    key='key_symptom'
                    )
        
            resolution = st.text_input(label="resolution: ", 
                    value=st.session_state.user_selected_row['resolution'],
                    on_change=lambda: setattr(
                        st.session_state,
                        'user_selected_row', 
                        st.session_state.key_resolution
                        ),
                    key='key_resolution'
                    )
            
            db_id = st.text_input(label="Id: ", 
                    value=st.session_state.user_selected_row['id'],
                    on_change=lambda: setattr(
                        st.session_state,
                        'user_selected_row', 
                        st.session_state.key_id
                        ),
                    key='key_id'
                    )
            
            submit_edit_button = st.button("Update This Entry", key="submit_edit_button")
            delete_button = st.button("Delete This Entry", key="delete_button")


            if submit_edit_button:
                data = {
                    'id': db_id,                    
                    'doc_type': doc_type,
                    'title': title,
                    'category': category,
                    'symptom': symptom,
                    'resolution': resolution                    
                    }
                database_control.update_single_row3(cnx, data)

            if delete_button:              
                database_control.delete_row(cnx, db_id)
 #-----------------------
        ###update_db_with_selected_rows(selected_rows)
        return {"selected_rows_indices": selected_indices, "selected_rows": selected_rows_df}
#-----------------------
    cnx = database_control.create_connection()
    df = pd.read_sql_query("SELECT * FROM tech_support", cnx)    

    st.subheader("A generic database open to the public for to help you with anything.")
    st.write("Feel free to contribute.")
    st.write("Select the 'Select' in the first column to 'update' or 'delete'.")
    st.page_link(page="pages/new.py", label="New Entry")
#     doc_types = database_control.doc_type_get_all(cnx)
#     popover_insert = st.popover("Add New", use_container_width=True)  
#     with popover_insert.form("New Entry", clear_on_submit=True):       
#         #res = database_control.doc_type_get_all(cnx)
#         #print("GET ALL DOC_TYPE: ",  res)
#         #date_created = st.date_input("Date Created")
#         title =popover_insert.text_input("Title: ")
#         doc_type = popover_insert.selectbox("Select one ", doc_types.title)
#         category = popover_insert.text_input("Category: ")
#         symptom = popover_insert.text_area("Symptom: ")
#         resolution = popover_insert.text_area("Resolution: ")

#         submit_new = popover_insert.form_submit_button('Submit')

#         if submit_new:
#             print("Title to save ", title)
#             database_control.add_row(cnx, title, doc_type, category, symptom, resolution)
#             st.success('Updated OK') 
# #           st.rerun()
    
    # VERSION 3.
#     doc_types = database_control.doc_type_get_all(cnx)
#     popover_insert = st.popover("Add New", use_container_width=True)  

#     # with popover_insert.form("New Entry", clear_on_submit=True):       
#     with st.form("Create New", clear_on_submit=True):
#         #res = database_control.doc_type_get_all(cnx)
#         #print("GET ALL DOC_TYPE: ",  res)
#         #date_created = st.date_input("Date Created")
#         title =popover_insert.text_input("Title: ")
#         doc_type = popover_insert.selectbox("Select one ", doc_types.title)
#         category = popover_insert.text_input("Category: ")
#         symptom = popover_insert.text_area("Symptom: ")
#         resolution = popover_insert.text_area("Resolution: ")

#         submit_new = popover_insert.form_submit_button('Submit')

#         if submit_new:
#             print("Title to save ", title)
#             database_control.add_row(cnx, title, doc_type, category, symptom, resolution)
#             st.success('Updated OK') 
# #           st.rerun()

    dataframe_with_selections(df)
    #selection = dataframe_with_selections(df)
    #st.write("Your selection:")
    #st.write(selection)