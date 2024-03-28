import streamlit as st
from streamlit_extras.badges import badge

def app():
     with st.container():
        colL, colM, colR = st.columns(3)
        with colL:
            pass
        with colM:
            st.write("Welcome to the..")
            st.markdown('''## :rainbow[Symbiotical.io]''')

            st.write("Cost: Free / Nothing.")
            st.write("")
            st.write("This site features..")

            st.write("- Find You Local Dog Parks")
            st.write("- Local Weather Forcast")
            st.write("And more to come..")
            st.write("Donations accepted! 😄")
            badge(type="buymeacoffee", name="ultimateselfhelp")

            st.write("")
            st.write("Send this link to others to invite and infom them of this site.")
            st.write("https://ultimate-self-help.onrender.com/")
        with colR:
            pass
        
    
