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
    if "show_edit_button" not in st.session_state:
        st.session_state.show_edit_button = False

    # if "user_selected_row" not in st.session_state:
    # st.session_state.user_selected_row = {}
    
    if "user_selected_title" not in st.session_state:
        st.session_state.user_selected_title = ""

    # if 'user_selected_row' not in st.session_state:
    #     st.session_state.user_selected_row = {}


    #does_db_and_tables_exist = False

    # Populate Update Form
    def callback_populate_form():
        #updated_row_df = st.session_state.user_selected_rows
        print("DATA CALLBACK: ", st.session_state.user_selected_row)

        #st.session_state.user_selected_title
        #return updated_row_df
        # return st.session_state.user_selected_title
        to_return = st.session_state.user_selected_row

        # WAS WORKING.
        #first_in_list = {}
        # if len(to_return) > 0:
        #     print("===> DATA CALLBACK: ", to_return )
        #     print("                                    ")
        #     print("===> DATA CALLBACK TITLE: ",type(to_return))
        #     first_in_list = list(to_return)[0]
        #     print("===> DATA CALLBACK TITLE LIST: ", first_in_list)
        # else:
        #     first_in_list = {}
        #print("GET ####################", first_in_list['title'])
        # return first_in_list
        return to_return
    

    def update_db_with_selected_rows(user_selected_rows):
        print("TO UPDATE 1: ", user_selected_rows) # [{}{}]
        print("TO UPDATE 2 ID: ", user_selected_rows['id'].values)
        row_dict = {}
        if len(user_selected_rows) < 1:
           row_dict = user_selected_rows.to_dict(orient='records')
        if len(user_selected_rows) > 0: 
            row_dict = user_selected_rows.to_dict(orient='records')
            row_dict = row_dict[0] # From list with multiple dicts to single dict.
        print("MY NEW DICT ====================> ", row_dict) # Now {}
              
        #print("ROW 2 : ", st.session_state.user_selected_row)
        st.session_state.user_selected_row =  row_dict
        print("DATA CALLBACK 4555: ", st.session_state.user_selected_row)


        #print("TO UPDATE 3: ", selected_rows['selected_rows'])

        #st.session_state.user_selected_row = user_selected_rows
        
        # CLEAN DATA.
        # print("selected_rows len: ", len(user_selected_rows))
        # if len(user_selected_rows) > 0:
        #     all = user_selected_rows.items()
        #     print("SINGLE ROW : ", all)
        #     #for row_list in user_selected_rows.items():
        #     for row_list in user_selected_rows.values:
        #         st.session_state.user_selected_row = row_list
        #         print("row_list: ", row_list)
        #         for value in row_list:
        #             print("EACH ROW: ", value)
        #     #     #st.session_state.user_selected_row = user_selected_rows[0]
        # else:
        #     st.session_state.user_selected_row = user_selected_rows

        # CLEAN DATA 2. BETTER. 
        # my_dict = {}
        # if len(user_selected_rows) < 1:
        #     pass
        # if len(user_selected_rows) > 0:
        #     print('TYPE PRE: ', type(user_selected_rows))
        #     #get_blah = user_selected_rows['title'].values[0] # Get only title column from row 0.
        #     get_blah = user_selected_rows.values[0]
        #     print("BLAH----> ", get_blah)
        #     print("selected_rows len: ", len(user_selected_rows))
        #     # [item for item in user_selected_row]
        #     for key, val in user_selected_rows[0]:
        #         my_dict.setdefault(key, val)
        # print("MY NEW DICT ====================> ", my_dict)

        #     for list in user_selected_rows.items():
        #         print("EACH ROW: ", list.value)

        #CLEAN DATA: BEST.
        # my_dict = {}
        # if len(user_selected_rows) < 1:
        #    pass
        # if len(user_selected_rows) > 0: 
        #     my_dict = user_selected_rows.to_dict(orient='records')
        # print("MY NEW DICT ====================> ", my_dict)
              
        # print("ROW 2 : ", st.session_state.user_selected_row)

        # WAS WORKING. print("SELECTED TITLE: ", st.session_state.user_selected_row['title'].values)
        ### st.session_state.user_selected_single = st.session_state.user_selected_row.values
        #st.session_state.user_selected_title = st.session_state.user_selected_row['title'].values
        #print("CLEANED title: ", st.session_state.user_selected_title)
        
        #print("=====> CLEANED title: ", st.session_state.user_selected_rows['title'][0])

        if len(user_selected_rows) > 0:
            st.session_state.show_edit_button = True


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

        # MY ADDITIONS
        # row_dict = {}
        # if len(selected_rows) < 1:
        #    row_dict = selected_rows.to_dict()
        # if len(selected_rows) > 0: 
        #     row_dict = selected_rows.to_dict()
        #     row_dict = row_dict[0] # From list with multip
        #row_dict = selected_rows.to_dict()

        #st.session_state.user_selected_row = row_dict
        ### list_to_dict = selected_rows.to_dict(orient='records')
        #st.session_state.user_selected_row = selected_rowslist_to_dict[0]
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
            # doc_type = st.selectbox("Select one ", doc_types.title, value=item_current['doc_types']['title'])
            # doc_type = st.selectbox("Select one ", doc_types.title) #.bug. Fix later.

            doc_type = st.selectbox("Doc Type: ", doc_types.title)
                    # value=st.session_state.user_selected_row['doc_type'],
                    # on_change=lambda: setattr(
                    #     st.session_state,
                    #     'user_selected_row', 
                    #     st.session_state.key_doc_type
                    #     ),
                    # key='key_doc_type'
                    # )
            
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
                    'key_cat',
                     st.session_state.user_selected_temp_key
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
            
            submit_edit_button = st.button("Submit", key="submit_edit_button")

            if submit_edit_button:
                print("EDIT: ", title)
                # if 'edited_row' not in st.session_state:
                #     st.session_state.edited_row = st.dataframe()
                
                # st.session_state.edited_row['id'] = db_id    
                # st.session_state.edited_row['doc_type'] = doc_type
                # st.session_state.edited_row['title'] = title
                # st.session_state.edited_row['category'] = category
                # st.session_state.edited_row['symptom'] = symptom
                # st.session_state.edited_row['resolution'] = resolution

                # Convert from session_state (df) to dataframe. Why?
                data = {
                    'id': db_id,                    
                    'doc_type': doc_type,
                    'title': title,
                    'category': category,
                    'symptom': symptom,
                    'resolution': resolution
                    }
                #df4 = st.dataframe(data)

                print("DF4: ", data)

                #database_control.update_single_row(cnx, title, doc_type, category, symptom, resolution)
                
                # database_control.update_single_row(cnx, 
                #     st.session_state["user_selected_id"],
                #     st.session_state["my_key"]
                # )
                #print("EDITED ROW: ", st.session_state.edited_row)
                #print("EDITED ROW: ", st.session_state.edited_row['id'])
                database_control.update_single_row3(cnx, data)



        #-----------------------
        ###update_db_with_selected_rows(selected_rows)
        return {"selected_rows_indices": selected_indices, "selected_rows": selected_rows_df}


    cnx = database_control.create_connection()
    df = pd.read_sql_query("SELECT * FROM tech_support", cnx)    

    st.subheader("Hi")

    doc_types = database_control.doc_type_get_all(cnx)
    popover_insert = st.popover("Add New", use_container_width=True)  
    with popover_insert.form("New Entry", clear_on_submit=True):
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
            
    # VERSION 1.
    # if st.session_state.show_edit_button: 
    #     popover_update = st.popover("Update", use_container_width=True)  
    #     with popover_update.form("Update Entry", clear_on_submit=True):
    #         item_current = callback_populate_form()
    #         if len(item_current):
    #             print("")
    #             print("CURRENT ITEM: ", item_current['title'])
    #             title = st.text_input("Title: ", value=item_current['title'])
    #             #doc_type = st.selectbox("Select one ", doc_types.title, value=item_current['doc_types']['title'])
    #             doc_type = st.selectbox("Select one ", doc_types.title) #.bug. Fix later.
    #             category = st.text_input("Category: ", value=item_current['category'])
    #             symptom = st.text_area("Symptom: ", value=item_current['symptom'])
    #             resolution = st.text_area("Resolution: ", item_current['resolution'])
            
    #         else:
    #             title = st.text_input("Title: ")
    #             doc_type = st.selectbox("Select one ", doc_types.title)
    #             category = st.text_input("Category: ")
    #             symptom = st.text_area("Symptom: " )
    #             resolution = st.text_area("Resolution: ")

    #         submit_update = st.form_submit_button("Update")

    #         if submit_update:
    #             print("Title to save ", title)
    #             # database_control.update_single_row(cnx, title, doc_type, category, symptom, resolution)
    #             # st.success('Updated OK') 
    #             # st.rerun()
            
    # VERSION 2.
    # popover_update = st.popover("Update", use_container_width=True)  
    # with st.form("Update Entry", clear_on_submit=True):
    #     item_current = callback_populate_form()
    #     if len(item_current):
    #         print("")
    #         print("CURRENT ITEM: ", item_current['title'])
    #         title = st.text_input("Title: ", value=item_current['title'])
    #         #doc_type = st.selectbox("Select one ", doc_types.title, value=item_current['doc_types']['title'])
    #         doc_type = st.selectbox("Select one ", doc_types.title) #.bug. Fix later.
    #         category = st.text_input("Category: ", value=item_current['category'])
    #         symptom = st.text_area("Symptom: ", value=item_current['symptom'])
    #         resolution = st.text_area("Resolution: ", item_current['resolution'])
        
    #     else:
    #         title = st.text_input("Title: ")
    #         doc_type = st.selectbox("Select one ", doc_types.title)
    #         category = st.text_input("Category: ")
    #         symptom = st.text_area("Symptom: " )
    #         resolution = st.text_area("Resolution: ")

    #     submit_update = st.form_submit_button("Update")

    #     if submit_update:
    #         print("Title to save ", title)
    #         # database_control.update_single_row(cnx, title, doc_type, category, symptom, resolution)
    #         # st.success('Updated OK') 
    #         # st.rerun()
            
    # VERSION 3.
    # with st.form("Update Form"):
        # temp = st.session_state.user_selected_row
        # print("TYPE OF ", temp)
        #print("TITLE zzzzzzz: ", st.session_state.user_selected_row['title'])
    # Initialize session state for 'ss_text' when the page first renders
    # if 'user_selected_row' not in st.session_state:
    #     st.session_state.user_selected_row = pd.DataFrame()
        # {
        #     'id':0,
        #     'date_created':'2024-03-01',
        #    'title': 'test'
        # }
        #st.session_state.user_selected_row = df

    
    # temp = st.session_state.user_selected_row
    # print ("TEMP1 : ", temp)
    # print("TEMP TYPE: ", type(temp))

    # if 'user_selected_row' not in st.session_state:
    #     print("TESSSSSSSSSSSSSSSST")
    #     title = st.text_input(label="Title: ", 
    #                             value=temp['title'],
    #                             on_change=lambda: setattr(st.session_state, 'user_selected_row', st.session_state.key_ss_text),
    #                             key='key_ss_text'
    #                             )
    #     st.write(f"You set ss_text to: `{title}`")

        # submit_update = st.form_submit_button("Update")

        # if submit_update:
        #     print("Title to save ", title)
        #     st.write(f"You set user_selected_row to: `{title}")
        #     # database_control.update_single_row(cnx, title, doc_type, category, symptom, resolution)
        #     # st.success('Updated OK') 
        #     # st.rerun()

            
    # if st.session_state.show_edit_button:
    #     st.button("Edit")

    dataframe_with_selections(df)
    #selection = dataframe_with_selections(df)
    #st.write("Your selection:")
    #st.write(selection)