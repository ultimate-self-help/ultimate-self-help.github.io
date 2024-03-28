import streamlit as st
from streamlit_extras.badges import badge
import streamlit.components.v1 as components

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
           
            st.write("Donations accepted! 😄")
            # badge(type="buymeacoffee", name="ultimateselfhelp")
            # components.html("<script type='text/javascript' src='https://storage.ko-fi.com/cdn/widget/Widget_2.js'></script><script type='text/javascript'>kofiwidget2.init('Support Me on Ko-fi', '#29abe0', 'W7W6W7JOT');kofiwidget2.draw();</script>", width=200, height=55)
            badge(type="buymeacoffee", name="symbiotical")
                 
            st.write("")
            st.write("Send this link to others to invite and inform them of this site.")
            st.write("https://symbiotical.io/")
           
        with colR:
            pass

        with st.container():
            st.write("This site features..")

        with st.container(border=True):
             colL, colR = st.columns(2)
        with colL:
            st.page_link(page="pages/dog_parks_about.py", label="Dog Parks")
            st.page_link(page="pages/where_am_i.py", label="Where Am I")
            st.page_link(page="pages/tools_weather.py", label="Weather")
            st.page_link(page="pages/donate.py", label="Donate")
            st.page_link(page="pages/about.py", label="About")
        with colR:
            st.write("Find dog parkes in you local area displayed on a map.")
            st.write("Lost? Display your GPS coordinates and location on map.")
            st.write("Get your local weather forcast.")
            st.write("Help keep this site alive and well.")
            st.write("One off read or overview about this site.")

