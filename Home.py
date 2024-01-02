import streamlit as st
# STREAMLIT HOME PAGE: https://docs.streamlit.io/library/api-reference#magic-commands

st.set_page_config(
    page_title="Ultimate-Self-Help",
    page_icon="👋",
    layout='wide'
)

st.title("Main Page")
# st.sidebar.success("Select a page above.")

# Global state (all pages)
# Source: https://www.youtube.com/watch?v=YClmpnpszq8&list=PL7QI8ORyVSCaejt2LICRQtOTwmPiwKO2n&index=14
if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)

