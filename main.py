import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import home as home
import pages.dog_parks_about as dog_parks_about
import pages.donate as donate
import pages.about as about
import pages.tools_about as tools_about
import pages.tools_weather as tools_weather
import pages.tech_support_about as tech_support_about

from st_pages import hide_pages, show_pages, Page

st.set_page_config(
    page_title="Ultimate-Self-Help",
    page_icon="🐶",
    layout='wide'
)

# Hide top right default 'deploy' menu for production.
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Hide specific pages from default sidebar.
hide_pages(["new","main", "home", "about", "tools_weather", "donate", "dog_parks_about","tech_support_about", "tools_about"])

if "my_input" not in st.session_state:
    st.session_state['my_input'] = ""

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.app.append({
            "title": title,
            "function": function
        })


    def run():
        with st.sidebar:
            # Icons from Twemoji. Failed.
            #OK. https://icons.getbootstrap.com/?q=house
            app = option_menu(
                menu_title='Welcome to USH',
                options=['Home','Dog Parks','Weather','Donate','About'],
                icons=['house','signpost-2','cloud-sun','piggy-bank', 'info-circle'],
                menu_icon='person-raised-hand',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
            "icon": {"color": "white", "font-size": "23px"}, 
            "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
            "nav-link-selected": {"background-color": "#02ab21"},}
            )

        if app == "Home":
            home.app()
        if app == "Donate":
            donate.app()    
        if app == "Dog Parks":
           dog_parks_about.app()        
        if app == 'Tech Support':
            tech_support_about.app()
        if app == "Tools":
           tools_about.app() 
        if app == "Weather":
           tools_weather.app() 
        if app == 'About':
            about.app()
    
    run()