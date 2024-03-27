import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

import pages.home as home
import pages.dog_parks_about as dog_parks_about
import pages.donate as donate
import pages.about as about
import pages.tools_about as tools_about
import pages.tools_weather as tools_weather
import pages.tech_support_about as tech_support_about

st.subheader("MENU")
# Move sidebar menu here.