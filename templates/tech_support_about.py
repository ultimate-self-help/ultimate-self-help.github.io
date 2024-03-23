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
import streamlit.components.v1 as stc
import numpy as np
#from datetime import datetim
### from streamlit_extras.dataframe_explorer import dataframe_explorer
#from streamlit_option_menu import option_menu 

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

        # DELETE.
        st.subheader('Delete single entry')
        id = st.number_input('Id to delete', value=0)
        if st.button('Delete Expense'):    
            database_control.delete_budget(cnx, int(id))
            st.success('Expense deleted!')
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
        st.write("Count: ", df_filtered['title'].count().round(2))

        # READ AND DISPLAY.
        inital_data_from_db = df
        st.write("NEW V2")
        # st.write(pd.DataFrame(inital_data_from_db, columns=["title", "category","symptom","resolution","Edit", "Delete" ]))


        # https://docs.streamlit.io/library/api-reference/data/st.data_editor
        # edited_df = st.data_editor(df, num_rows="dynamic")
        # favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
        # st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

        # for item in df:
        #     st.write("Row: ", item)

        # ------------------------ SEMI WORKING ------------------------------
        # https://discuss.streamlit.io/t/deleting-rows-in-st-data-editor-progmatically/46337
        # if "data" not in st.session_state:
        #     # st.session_state.data = pd.DataFrame(
        #     #     {"title": [1, 2, 3, 4], "category": [10, 20, 30, 40]}
        #     # )
        #     st.session_state.data = pd.DataFrame(df)

        # def delete_selected():
        #     edited_rows = st.session_state["data_editor"]["edited_rows"]
        #     rows_to_delete = []

        #     for idx, value in edited_rows.items():
        #         if value["x"] is True:
        #             rows_to_delete.append(idx)

        #     st.session_state["data"] = (
        #         st.session_state["data"].drop(rows_to_delete, axis=0).reset_index(drop=True)
        #     )

        # # BACKUP . WORKING.
        # # def callback():
        # #     edited_rows = st.session_state["data_editor"]["edited_rows"]
        # #     rows_to_delete = []

        # #     for idx, value in edited_rows.items():
        # #         if value["x"] is True:
        # #             rows_to_delete.append(idx)

        # #     st.session_state["data"] = (
        # #         st.session_state["data"].drop(rows_to_delete, axis=0).reset_index(drop=True)
        # #     )
            
        # def callback():
        #     edited_rows = st.session_state["data_editor"]["edited_rows"]
        #     rows_to_delete = []

        #     # Get dataframe row-selections from user with st.data_editor
        #     df_with_selections = df.copy()
        #     # # df_with_selections.insert(0, "Select", False)
        #     edited_df = st.data_editor(
        #         df_with_selections,
        #         hide_index=True,
        #     #     column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        #     #     disabled=df.columns,
        #     )
        #     #selected_rows = edited_df[edited_df.Select]


        #     selected_rows = edited_rows
        #     st.write("Selected: ", selected_rows)

           

        # # https://docs.streamlit.io/knowledge-base/using-streamlit/how-to-get-row-selections
        # columns = st.session_state["data"].columns
        # column_config = {column: st.column_config.Column(disabled=True) for column in columns}

        # modified_df = st.session_state["data"].copy()
        # #modified_df.insert(0, "Select", False)
        # modified_df["x"] = False
        # # Make Delete be the first column
        # modified_df = modified_df[["x"] + modified_df.columns[:-1].tolist()]


        # st.data_editor(
        #     modified_df,
        #     key="data_editor",
        #     on_change=callback,
        #     hide_index=True,
        #     column_config=column_config,
        # )
        #---------------------------------------------------------
        
        # df2 = pd.DataFrame(
        #     {
        #         "Animal": ["Lion", "Elephant", "Giraffe", "Monkey", "Zebra"],
        #         "Habitat": ["Savanna", "Forest", "Savanna", "Forest", "Savanna"],
        #         "Lifespan (years)": [15, 60, 25, 20, 25],
        #         "Average weight (kg)": [190, 5000, 800, 10, 350],
        #     }
        # )

        # def dataframe_with_selections(df2):
        #     df_with_selections = df2.copy()
        #     df_with_selections.insert(0, "Select", False)

        #     # Get dataframe row-selections from user with st.data_editor
        #     edited_df = st.data_editor(
        #         df_with_selections,
        #         hide_index=True,
        #         column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        #         disabled=df2.columns,
        #     )

        #     # Filter the dataframe using the temporary column, then drop the column
        #     selected_rows = edited_df[edited_df.Select]
        #     return selected_rows.drop('Select', axis=1)

        # selection = dataframe_with_selections(df2)
        # st.write("Your selection:")
        # st.write(selection)


        #-------------------------------------------------------
        # st.rerun()

        #---------------
        # filtered_dfe = dataframe_explorer(df)
        # st.dataframe(filtered_dfe, use_container_width=False)

        # PYGWALKER. TABLEAU
        # By Category (Coloured Metchant). Large.
        #by_category = r"""{"config":[{"config":{"defaultAggregated":true,"geoms":["bar"],"coordSystem":"generic","limit":-1},"encodings":{"dimensions":[{"dragId":"gw_16zm","fid":"Date","name":"Date","basename":"Date","semanticType":"nominal","analyticType":"dimension"},{"dragId":"gw__SWI","fid":"Account Number","name":"Account Number","basename":"Account Number","semanticType":"quantitative","analyticType":"dimension"},{"dragId":"gw_VZtJ","fid":"Unnamed: 3","name":"Unnamed: 3","basename":"Unnamed: 3","semanticType":"nominal","analyticType":"dimension"},{"dragId":"gw_prCo","fid":"Transaction Type","name":"Transaction Type","basename":"Transaction Type","semanticType":"nominal","analyticType":"dimension"},{"dragId":"gw_3Pmq","fid":"Transaction Details","name":"Transaction Details","basename":"Transaction Details","semanticType":"nominal","analyticType":"dimension"},{"dragId":"gw_md8y","fid":"Category","name":"Category","basename":"Category","semanticType":"nominal","analyticType":"dimension"},{"dragId":"gw_x3Qd","fid":"Merchant Name","name":"Merchant Name","basename":"Merchant Name","semanticType":"nominal","analyticType":"dimension"},{"dragId":"gw_mea_key_fid","fid":"gw_mea_key_fid","name":"Measure names","analyticType":"dimension","semanticType":"nominal"}],"measures":[{"dragId":"gw_xml5","fid":"Amount","name":"Amount","basename":"Amount","analyticType":"measure","semanticType":"quantitative","aggName":"sum"},{"dragId":"gw_v14k","fid":"Balance","name":"Balance","basename":"Balance","analyticType":"measure","semanticType":"quantitative","aggName":"sum"},{"dragId":"gw_count_fid","fid":"gw_count_fid","name":"Row count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","computed":true,"expression":{"op":"one","params":[],"as":"gw_count_fid"}},{"dragId":"gw_mea_val_fid","fid":"gw_mea_val_fid","name":"Measure values","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"rows":[{"dragId":"gw_IUYe","fid":"Category","name":"Category","basename":"Category","semanticType":"nominal","analyticType":"dimension","sort":"descending"}],"columns":[{"dragId":"gw_1CEk","fid":"Amount","name":"Amount","basename":"Amount","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"color":[{"dragId":"gw_cecO","fid":"Merchant Name","name":"Merchant Name","basename":"Merchant Name","semanticType":"nominal","analyticType":"dimension"}],"opacity":[],"size":[],"shape":[],"radius":[],"theta":[],"longitude":[],"latitude":[],"geoId":[],"details":[],"filters":[{"dragId":"gw_0IrI","fid":"Date","name":"Date","basename":"Date","semanticType":"nominal","analyticType":"dimension","rule":null},{"dragId":"gw_aTxA","fid":"Amount","name":"Amount","basename":"Amount","analyticType":"measure","semanticType":"quantitative","aggName":"sum","rule":{"type":"range","value":[-500,500]}}],"text":[]},"layout":{"showActions":false,"showTableSummary":false,"stack":"stack","interactiveScale":false,"zeroScale":true,"size":{"mode":"fixed","width":601,"height":375},"format":{},"geoKey":"name","resolve":{"x":false,"y":false,"color":false,"opacity":false,"shape":false,"size":false}},"visId":"gw_ZKkM","name":"Chart 1"}],"chart_map":{},"workflow_list":[{"workflow":[{"type":"filter","filters":[{"fid":"Amount","rule":{"type":"range","value":[-500,500]}}]},{"type":"view","query":[{"op":"aggregate","groupBy":["Category","Merchant Name"],"measures":[{"field":"Amount","agg":"sum","asFieldKey":"Amount_sum"}]}]}]}],"timezoneOffsetSeconds":39600,"version":"0.3.20"}"""
        # pyg_html = pyg.walk(df,  spec=by_category, return_html=True, dark='light')
        #pyg_html = pyg.walk(df, return_html=True)
        ### pyg_html = pyg.walk(df, return_html=True)
        ### stc.html(pyg_html, scrolling=True, height=1000)
        #--------------------------------------------------------
        # VERSION 11.
        
        # st.write('Dataframe:')
        # st.dataframe(df)

        # Add a multiselect widget to select rows based on the index
        # selected_indices = st.multiselect('Select rows:', df.index)

        # Subset the dataframe with the selected indices
        # selected_rows = df.loc[selected_indices]

        # Display the selected data
        # st.write('Selected Rows:')
        # st.dataframe(selected_rows)

    # If DB or tables do not pre-exist. Create it.
    # except:
    #     submit = st.button("Create DB (First Time Users)")
    #     if submit:
    #         database_control.create_db_and_tables()
    #     st.write("DB does not exist yet! Create it first!")
    #-------------------- ORIGINAL WORKING ----------------------------
        # if "data" not in st.session_state:
        #         # st.session_state.data = pd.DataFrame(
        #         #     {"title": [1, 2, 3, 4], "category": [10, 20, 30, 40]}
        #         # )
        #         st.session_state.data = pd.DataFrame(df)

        # # BACKUP . WORKING.
        # def callback():
        #     edited_rows = st.session_state["data_editor"]["edited_rows"]
        #     rows_to_delete = []

        #     for idx, value in edited_rows.items():
        #         if value["x"] is True:
        #             rows_to_delete.append(idx)

        #     st.session_state["data"] = (
        #         st.session_state["data"].drop(rows_to_delete, axis=0).reset_index(drop=True)
        #     )       
        #     #selected_rows = edited_df[edited_df.Select]
        #     selected_rows = edited_rows
        #     st.write("Selected: ", selected_rows)

        # # https://docs.streamlit.io/knowledge-base/using-streamlit/how-to-get-row-selections
        # columns = st.session_state["data"].columns
        # column_config = {column: st.column_config.Column(disabled=True) for column in columns}

        # modified_df = st.session_state["data"].copy()
        # #modified_df.insert(0, "Select", False)
        # modified_df["x"] = False
        # # Make Delete be the first column
        # modified_df = modified_df[["x"] + modified_df.columns[:-1].tolist()]


        # st.data_editor(
        #     modified_df,
        #     key="data_editor",
        #     on_change=callback,
        #     hide_index=True,
        #     column_config=column_config,
        # )
    #-------------------------------------------------
        # def callback(index):
        #     st.write("User selected index: ",index)

        # columns = st.session_state["data"].columns
        # column_config = {column: st.column_config.Column(disabled=True) for column in columns}
        
        # modified_df = st.session_state["data"].copy()
        # #modified_df.insert(0, "Select", False)
        # modified_df["x"] = False
        # # Make Delete be the first column
        # modified_df = modified_df[["x"] + modified_df.columns[:-1].tolist()]

        # st.data_editor(
        #     modified_df,
        #     key="data_editor",
        #     on_change=callback(modified_df),
        #     hide_index=True,
        #     column_config=column_config,
        # )   
        # # Add a multiselect widget to select rows based on the index
        # selected_indices = st.multiselect('Select rows:', df.index)

        # # Display the selected data
        # st.write('Selected Rows:')
        # st.dataframe(selected_rows)
        #----------------------------------------------
        # https://blog.streamlit.io/editable-dataframes-are-here/
        # edited_df = st.data_editor(
        #     df,
        #     num_rows=”dynamic”
        #     )
        # favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
        # st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
        #================================
        # BEST EXAMPLE: https://discuss.streamlit.io/t/how-to-select-single-or-multiple-rows-in-st-dataframe-and-return-the-selected-data/54897/4
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
            #st.write("Selected Rows: ", edited_df.loc["title"])
            st.write("Hello", edited_df[edited_df.Select]['id'])
            #print("RESULT: ", edited_df[edited_df.Select])
            #favorite_command = edited_df.loc[edited_df["title"]]["command"]   
            #st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
            return selected_rows.drop('Select', axis=1)
    
        def get_selected_id():
            pass

        selection = dataframe_with_selections(df)
        st.write("Your selection:")
        st.write(selection)
        # st.write(selection.loc)
    except:
        pass


