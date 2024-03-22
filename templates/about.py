import streamlit as st

def app():
    # Source: https://www.youtube.com/watch?v=VqgUkExPvLY
    # st.set_page_config(
    #     page_title="About", 
    #     page_icon=":tada:", 
    #     layout="wide"
    # )

    st.title("About")
    st.write("This site is a one man hobby and a constant work in progress. Watch this space!")
    st.write("This site will be taken offline if any signs of technical abuse or heavy financial loss.")
    st.write()
    st.write("Started: 2024Jan02")
    st.write("Last update: 2024Mar21.")

    st.write("Features will grow over time.")
            
        # st.write("Under construction, come back soon 2024.")
    if st.session_state:
        st.write(" You entered " , st.session_state["my_input"])