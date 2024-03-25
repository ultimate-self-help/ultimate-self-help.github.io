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
    # If DB or tables do not exist. Create them.
    # cnx = ""
    # df = ""
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
        st.write("DB does not exist yet! Create it first!")
        #print("does_db_and_tables_exist 2 : ", does_db_and_tables_exist)

    # DISPLAY TABLE ----------------
    #print("does_db_and_tables_exist 3 : ", does_db_and_tables_exist)
    if does_db_and_tables_exist:
        try:
            cnx = database_control.create_connection()
            df = pd.read_sql_query("SELECT * FROM tech_support", cnx)

            with st.container(border=True):
                # title = st.multiselect(
                #     "Filter by Title:",
                #     options=df["title"].unique(),
                #     default=df["title"].unique(),
                # )

                # New record. Create.            
                popover = st.popover("Add New", use_container_width=True)  
                res = database_control.doc_type_get_all(cnx)
                with popover.form("New Entry"):
                    #res = database_control.doc_type_get_all(cnx)
                    #print("GET ALL DOC_TYPE: ",  res)
                    #date_created = st.date_input("Date Created")
                    title = popover.text_input("Title: ")
                    doc_type = popover.selectbox("Select one ", res.title)
                    category = popover.text_input("Category: ")
                    symptom = popover.text_area("Symptom: ")
                    resolution = popover.text_area("Resolution: ")
                    submit = popover.button('Submit')
                    #print("Selected: ", doc_type)

                    if submit:
                        print("Title to save ", title)
                        database_control.add_row(cnx, title, doc_type, category, symptom, resolution)
                        st.success('Updated OK') 
                        st.rerun()

                # MANUAL FILTER. USING BELOW STREAMLIT EXPLORER INSTEAD.
                # category = st.multiselect(
                #     "Filter by Category:",
                #     options=df["category"].unique(),
                #     default=df["category"].unique(),
                # )
                # # df_filtered = df.query(
                # #     # "title == @title",
                # #     "category == @category"
                # # )

                # title = st.multiselect(
                #     "Filter by Title:",
                #     options=df["title"].unique(),
                #     default=df["title"].unique(),
                # )

                # df_filtered = df.query(
                #     "title == @title & category == @category"
                # )
                        
                # # COUNT OF ROWS.                
                # st.metric("Stats: ", df_filtered['title'].count().round(2))


                # BEST EXAMPLE: https://discuss.streamlit.io/t/how-to-select-single-or-multiple-rows-in-st-dataframe-and-return-the-selected-data/54897/4
                if "data" not in st.session_state:
                    # Array of row Id's in prep to delete from DB.
                    st.session_state.data = []


                def dataframe_with_selections(df: pd.DataFrame, init_value: bool = False) -> pd.DataFrame:
                    df_with_selections = df.copy()
                    df_with_selections.insert(0, "Select", init_value)

                    # Get dataframe row-selections from user with st.data_editor
                    edited_df = st.data_editor(
                        df_with_selections,
                        hide_index=True,
                        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
                        disabled=df.columns,
                        num_rows="dynamic",
                        
                    )

                    # Filter the dataframe using the temporary column, then drop the column
                    selected_rows = edited_df[edited_df.Select]
                    st.session_state.data = edited_df[edited_df.Select]['id']
                    return selected_rows.drop('Select', axis=1)            

                # DELETE ROW.
                def delete_row():
                    ids_to_delete = st.session_state.data
                    res = database_control.delete_row(cnx, ids_to_delete)
                    return res 
                
                selection = dataframe_with_selections(df)
                st.write("You selected to delete:")
                st.write(selection)


                submit = st.button("Delete selected row(s)")
                if submit:
                    res = delete_row()
                    return res
                
                # # PGY WALKER. TABLEAU. WORKING OK----------------------------------
                # # PGY WALKER: (Old)
                # # Generate the HTML using Pygwalker
                # ### pyg_html = pyg.to_html(df)
                # # Embed the HTML into the Streamlit app
                # ###components.html(pyg_html, height=1000, scrolling=True)

                # # PYG WALKER (NEW)
                # # Source: https://docs.kanaries.net/pygwalker/use-pygwalker-with-streamlit
                # # Establish communication between pygwalker and streamlit
                # init_streamlit_comm()
                
                # # Get an instance of pygwalker's renderer. You should cache this instance to effectively prevent the growth of in-process memory.
                # @st.cache_resource
                # def get_pyg_renderer() -> "StreamlitRenderer":
                #     #df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")
                #     # When you need to publish your app to the public, you should set the debug parameter to False to prevent other users from writing to your chart configuration file.
                #     return StreamlitRenderer(df, spec="./gw_config.json", debug=False)
                
                # renderer = get_pyg_renderer()
                
                # # Render your data exploration interface. Developers can use it to build charts by drag and drop.
                # renderer.render_explore()
                # #--------------------------------------------

                # update.
                def callbackupdate(update):
                    print("UPdate: ", update)
                    
                

                st.markdown("## UPDATE ITEM/ROW")
                update_table = st.data_editor(
                    df, 
                    num_rows='dynamic',
                    key="my_key"
                )
                # Good Demo To Use Later:
                #https://streamlit-feature-demos-data-editor-foundationdemo-bhdzga.streamlit.app/#compatible-with-st-form

                # Closest: https://stackoverflow.com/questions/76445570/keep-getting-a-key-error-when-using-the-data-editor-streamlit

                # BEST FOR EXTRACT SINGLE CELL CHANGED ON ST.DATA_EDITOR()
                # https://docs.streamlit.io/library/advanced-features/dataframes#access-edited-data

                print("UPDATED TABLE 1: ", update_table)
                print("UPDATED TABLE 2: ", update_table.id)
                print("UPDATED TABLE 3: ", update_table.title)       
                print("INDEX: ", update_table.index)
                print("GET SINGLE ROW: ", update_table.loc[update_table.index])
                
                print("MY_KEY SESSION STATE: ", st.session_state["my_key"])
                database_control.update_single_row(cnx, st.session_state["my_key"])
                print("----------------")
                print("----------------")
                    

                # DATAFRAME EXPLORER. TEMP DISABLED. GOOD.
                # filtered_df = dataframe_explorer(df, case=False)
                # st.dataframe(filtered_df, use_container_width=True)

        except ImportError as e:
            print("DB Error: ", e)
