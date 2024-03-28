import streamlit as st
import streamlit.components.v1 as components
# from dependancies import sign_up, sign_in, fetch_users
from images import *
def app():

    st.title("Where Am I?")
    
    with st.expander("Help"):
        col1, col2, col3 = st.columns(3)
        with col2:
            st.subheader("Where Am I?")
        #st.page_link("dogparks2.py", icon="🐶", label="DogParks2")
        # st.page_link("dog_parks_map.py", label="Dog Park. Map", icon="🐶")
        st.write("If you are lost i.e. in an emergency you can use this to inform others of you GPS coordinates (latitude and longditue)")

        st.write("Warning: Data accuracy can not be garanteed")
        st.write("The source data is from public entering into google.com.")
        st.write("It may not be accurate i.e. Old information incorrect labeling of 'off-leash' etc.")

    HtmlFile = open("where_am_i.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    components.html(source_code, height=900, scrolling=False)