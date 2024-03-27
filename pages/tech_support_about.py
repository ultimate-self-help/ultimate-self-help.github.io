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
    does_db_and_tables_exist = False
    try:
        cnx = database_control.create_connection()
        df = pd.read_sql_query("SELECT * FROM tech_support", cnx)       
        does_db_and_tables_exist = True
        #print("does_db_and_tables_exist 1 : ", does_db_and_tables_exist)
    except:
        does_db_and_tables_exist = False
        submit = st.button("Create DB (First Time Users)")
        if submit:
            database_control.create_db_and_tables()
            st.switch_page("main")
        st.write("DB does not exist yet! Create it first!")



    if does_db_and_tables_exist:     
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
                print("1. EDITED_DF: ", selected_rows_df.iloc[0])
                st.session_state.user_selected_row = selected_rows_df.iloc[0]
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
            
                resolution = st.text_input(label="Resolution: ", 
                        value=st.session_state.user_selected_row['resolution'],
                        on_change=lambda: setattr(
                            st.session_state,
                            'user_selected_row', 
                            st.session_state.key_resolution
                            ),
                        key='key_resolution'
                        )
                
                db_id = st.text_input(label="Id: ",
                        disabled=True, 
                        value=st.session_state.user_selected_row['id'],
                        on_change=lambda: setattr(
                            st.session_state,
                            'user_selected_row', 
                            st.session_state.key_id
                            ),
                        key='key_id'
                        )
                
                link1 = st.text_input(label="Link: ", 
                        value=st.session_state.user_selected_row['link1'],
                        on_change=lambda: setattr(
                            st.session_state,
                            'user_selected_row', 
                            st.session_state.key_link1
                            ),
                        key='key_link1'
                        )
                
                rating = st.number_input(label="Rating: ", 
                        value=st.session_state.user_selected_row['rating'],
                        on_change=lambda: setattr(
                            st.session_state,
                            'user_selected_row', 
                            st.session_state.key_rating
                            ),
                        key='key_rating'
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
                        'resolution': resolution,                    
                        'link1': link1,          
                        'rating': rating
                        }
                    database_control.update_single_row3(cnx, data)

                if delete_button:              
                    database_control.delete_row(cnx, db_id)

            return {"selected_rows_indices": selected_indices, "selected_rows": selected_rows_df}

    #-----------------------
        cnx = database_control.create_connection()
        df = pd.read_sql_query("SELECT * FROM tech_support", cnx)    
        doc_types = database_control.doc_type_get_all(cnx)

        st.subheader("Self Help DB")
        
        with st.expander("Help"):
            st.write("A generic database open for the public to assist in you daily lives with anything.")
            st.write("Select the 'Select' in the first column to 'update' or 'delete'. Feel free to contribute.")
            st.write("This is a work in progress. Be gentle.")
            
        
        if st.button("Create New"):
            st.switch_page("pages/new.py")

        # Display main matrix.
        #         data_df = pd.DataFrame(
        #     {
        #         "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
        #     }
        # )

        # st.dataframe(
        #     data_df,
        #     column_config={
        #         "widgets": st.column_config.Column(
        #             width="medium"
        #         )
        #     }
        # )

        #st.container("Generic DB to self help")
        dataframe_with_selections(df)
        #selection = dataframe_with_selections(df)
        #st.write("Your selection:")
        #st.write(selection)