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

def app():
    cnx = database_control.create_connection()
    # DISPLAY TABLE ----------------
    try:
        cnx = database_control.create_connection()
        df = pd.read_sql_query("SELECT * FROM tech_support", cnx)
        # title = st.multiselect(
        #     "Filter by Title:",
        #     options=df["title"].unique(),
        #     default=df["title"].unique(),
        # )

        # CREATE.
        with st.expander("Add new entry"):
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


        category = st.multiselect(
            "Filter by Category:",
            options=df["category"].unique(),
            default=df["category"].unique(),
        )
        # df_filtered = df.query(
        #     # "title == @title",
        #     "category == @category"
        # )

        title = st.multiselect(
            "Filter by Title:",
            options=df["title"].unique(),
            default=df["title"].unique(),
        )

        df_filtered = df.query(
            "title == @title & category == @category"
        )
                
        # COUNT OF ROWS.                
        st.metric("Stats: ", df_filtered['title'].count().round(2))
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
        

        # PGY WALKER: (Old)
        # Generate the HTML using Pygwalker
        ### pyg_html = pyg.to_html(df)
        # Embed the HTML into the Streamlit app
        ###components.html(pyg_html, height=1000, scrolling=True)

        # PYG WALKER (NEW)
        # Establish communication between pygwalker and streamlit
        init_streamlit_comm()
        # Get an instance of pygwalker's renderer. You should cache this instance to effectively prevent the growth of in-process memory.
        @st.cache_resource
        def get_pyg_renderer() -> "StreamlitRenderer":
            #df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")
            # When you need to publish your app to the public, you should set the debug parameter to False to prevent other users from writing to your chart configuration file.
            return StreamlitRenderer(df, spec="./gw_config.json", debug=False)
        
        renderer = get_pyg_renderer()
        
        # Render your data exploration interface. Developers can use it to build charts by drag and drop.
        renderer.render_explore()

    except:
        pass