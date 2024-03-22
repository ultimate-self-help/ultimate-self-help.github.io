import streamlit as st

def app():

    st.write("Tools")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Link")
            # st.page_link("pages/tools-clean-text.py", label="Clean Text")        
        


        with right_column:
            st.header("Description")
            st.write(
                """
                Remove 'wierd charactors' from text e.g. carriage returns.
                """
            )


