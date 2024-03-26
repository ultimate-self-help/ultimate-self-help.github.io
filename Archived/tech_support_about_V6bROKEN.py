# WORKING. 
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
    # def update_customer(name, address, phone):
    #     conn = sqlite3.connect('customers.db')
    #     c = conn.cursor()
    #     c.execute("UPDATE customers SET address = ?, phone = ? WHERE name = ?", (address, phone, name))
    #     conn.commit()
    #     conn.close()

    # if "user_selected_row" not in st.session_state:
    #     st.session_state.user_selected_row = []


#------------------ END OF FUNCTIONS ------------------------
    st.session_state.show_edit_button = True
    st.session_state.user_selected_row = []
    does_db_and_tables_exist = False

    #print("STATUS SHOW EDIT BTN: ",st.session_state.show_edit_button )

    def update_db_with_selected_rows(selected_rows):
        print("TO UPDATE 1: ", selected_rows)
        print("TO UPDATE 2: ", selected_rows['id'].values)
        #print("TO UPDATE 3: ", selected_rows['selected_rows'])

        st.session_state.user_selected_row = selected_rows['selected_rows']
        print("SELECTED: ", st.session_state.user_selected_row)
                
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
        st.write("DB does not exist yet! Create it first!")


    if does_db_and_tables_exist:
        st.subheader("Hello")
        try:
            cnx = database_control.create_connection()
            df = pd.read_sql_query("SELECT * FROM tech_support", cnx)

            selection = dataframe_with_selections(df)
            st.write("Your selection:")
            st.write(selection)

            # if st.session_state.show_edit_button:
            #     st.button("Edit")

            # if st.session_state.show_edit_button:
            #     st.session_state.show_edit_button = False            
            #st.session_state.edit_button = False
            
            # ADD NEW ROW.
            ### doc_types = database_control.doc_type_get_all(cnx)
            # CREATE NEW.
    #         popover_insert = st.popover("Add New", use_container_width=True)  
    #         with popover_insert.form("New Entry"):
    #             #res = database_control.doc_type_get_all(cnx)
    #             #print("GET ALL DOC_TYPE: ",  res)
    #             #date_created = st.date_input("Date Created")
    #             title =popover_insert.text_input("Title: ")
    #             doc_type = popover_insert.selectbox("Select one ", doc_types.title)
    #             category = popover_insert.text_input("Category: ")
    #             symptom = popover_insert.text_area("Symptom: ")
    #             resolution = popover_insert.text_area("Resolution: ")
    #             submit = popover_insert.button('Submit')

    #             if submit:
    #                 print("Title to save ", title)
    #                 database_control.add_row(cnx, title, doc_type, category, symptom, resolution)
    #                 st.success('Updated OK') 
    # #               st.rerun()


            # if st.session_state.edit_button == False:
            #     with st.container(border=True):
            #         doc_types = database_control.doc_type_get_all(cnx)

            #         # CREATE NEW.
            #         popover_insert = st.popover("Add New", use_container_width=True)  
            #         with popover_insert.form("New Entry"):
            #             #res = database_control.doc_type_get_all(cnx)
            #             #print("GET ALL DOC_TYPE: ",  res)
            #             #date_created = st.date_input("Date Created")
            #             title =popover_insert.text_input("Title: ")
            #             doc_type = popover_insert.selectbox("Select one ", doc_types.title)
            #             category = popover_insert.text_input("Category: ")
            #             symptom = popover_insert.text_area("Symptom: ")
            #             resolution = popover_insert.text_area("Resolution: ")
            #             submit = popover_insert.button('Submit')

            #             if submit:
            #                 print("Title to save ", title)
            #                 database_control.add_row(cnx, title, doc_type, category, symptom, resolution)
            #                 st.success('Updated OK') 
            #                 st.rerun()
    
            #doc_types = database_control.doc_type_get_all(cnx)
            #UPDATE
            #popover_update = st.popover("Update Entry", use_container_width=True)  
            #popover_update = st.container()
            #with st.container(border=True):
            # st.session_state.show_edit_button = False
                
            # if st.session_state.edit_button:
            #     doc_types = database_control.doc_type_get_all(cnx)
            #     # CREATE NEW.
            #     popover_insert = st.popover("Add New", use_container_width=True)  
            #     with popover_insert.form("New Entry"):
            #         #res = database_control.doc_type_get_all(cnx)
            #         #print("GET ALL DOC_TYPE: ",  res)
            #         #date_created = st.date_input("Date Created")
            #         title =popover_insert.text_input("Title: ")
            #         doc_type = popover_insert.selectbox("Select one ", doc_types.title)
            #         category = popover_insert.text_input("Category: ")
            #         symptom = popover_insert.text_area("Symptom: ")
            #         resolution = popover_insert.text_area("Resolution: ")
            #         submit = popover_insert.button('Submit')

            #         if submit:
            #             print("Title to save ", title)
            #             database_control.add_row(cnx, title, doc_type, category, symptom, resolution)
            #             st.success('Updated OK') 
            #             st.rerun()

            # GOOD----------------
            # if st.session_state.show_edit_button:                        
            #     with st.form("Update Entry"):
            #         #res = database_control.doc_type_get_all(cnx)
            #         #print("GET ALL DOC_TYPE: ",  res)
            #         #date_created = st.date_input("Date Created")
            #         print("SELECTED TITLE: ", st.session_state.user_selected.row)
            #         title = st.text_input("Title: ")
            #         doc_type = st.selectbox("Select one ", doc_types.title)
            #         category = st.text_input("Category: ")
            #         symptom = st.text_area("Symptom: ")
            #         resolution = st.text_area("Resolution: ")
            #         submit_update = st.form_submit_button("Update")

            #         if submit_update:
            #             print("Title to save ", title)
            #             # database_control.update_single_row(cnx, title, doc_type, category, symptom, resolution)
            #             # st.success('Updated OK') 
            #             # st.rerun()
            

            # def show_user_selected_row():
            #     print("USER SELECTED ROW: ", st.session_state.user_selected_row)
            #     print("USER SELECTED ROW: ", st.session_state.user_selected_row['edited_rows'])
                                
            # edited = st.data_editor(
            #     df,
            #     hide_index=True,
            #     num_rows="dynamic",
            #     use_container_width=True,
            #     key="user_selected_row",
            #     on_change=show_user_selected_row,
            # )
            #print("EDITED 1: ", edited.loc[edited.index])
        except:
            print("ERRRORRRRRRRRRRR")