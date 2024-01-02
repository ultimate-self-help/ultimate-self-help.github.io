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
            "Under construction, come back soon 2024."
            """
        )
        st.write("[Google ](https://google.com)")


    with right_column:
            st.header("Right")
         
    # st.write("Under construction, come back soon 2024.")