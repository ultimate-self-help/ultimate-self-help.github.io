import streamlit as st

# Source: https://www.youtube.com/watch?v=VqgUkExPvLY
st.set_page_config(
    page_title="About", 
     page_icon=":tada:", 
    layout="wide"
)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Left")
        st.write('##')
        st.write(
            """
            Under construction, come back soon 2024.
            This site will be open to public, free, no sign in
            for all use and contribute (via GitHub).
            i.e. Life tips and tricks, starting with technical info.
            """
        )
       


    with right_column:
            st.header("Right")
         
    # st.write("Under construction, come back soon 2024.")