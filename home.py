import streamlit as st
from streamlit_extras.badges import badge

def app():
     with st.container():
        colL, colM, colR = st.columns(3)
        with colL:
            pass
        with colM:
            st.write("Welcome to the..")
            st.markdown('''## :rainbow[Ultimate Self Help]''')

            st.write("Cost: Free / Nothing.")
            st.write("")
            st.write("A simple site for simple people!")
            st.write("This site has a multitude of different uses..")

            st.write("- Find You Local Dog Parks")
            st.write("- Local Weather Forcast")
            st.write("- Daily Usefull Tools (TBA)")
            st.write("Donations accepted! 😄")
            badge(type="buymeacoffee", name="ultimateselfhelp")

            st.write("")
            st.write("Send this link to others to invite and infom them of this site.")
            st.write("https://ultimate-self-help.onrender.com/")
        with colR:
            pass
        
    
