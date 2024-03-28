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
import pages.where_am_i as where_am_i
from streamlit_extras.badges import badge

from st_pages import hide_pages, show_pages, Page

st.set_page_config(
    page_title="Symbiotical.io",
    page_icon="🐶",
    layout='wide'
)

# Hide top right default 'deploy' menu for production.
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)

# Hide specific pages from default sidebar.
hide_pages(["new","main", "home", "where_am_i", "about", "tools_weather", "donate", "dog_parks_about","tech_support_about", "tools_about"])

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

            # Alternate Menu Option: Sub Dir.
            #https://discuss.streamlit.io/t/trick-simple-multpage/26121
            
            # Close sidebar menu 'X'.
            st.markdown("""<style>
            .st-emotion-cache-ch5dnh {
                    display: block;
                    min-width: 100%;
                        background-color: #4d90fe;
                        
                }
            </style>
            """, unsafe_allow_html=True)

            # Open Sidebar menu.
            st.markdown("""<style>
            .st-emotion-cache-6q9sum {
                    display: block;
                    -webkit-box-align: center;
                    align-items: center;
                    -webkit-box-pack: center;
                    justify-content: center;
                    font-weight: 400;
                    border-radius: 0.5rem;
                    margin: 0px 0.125rem;
                    color: white;
                    width: 100%;
                    user-select: none;
                    background-color: #4d90fe;
                    border: 2px;
                    font-size: 14px;
                    line-height: 1;
                    min-width: 100%;
                    min-height: 6rem;
                    padding: 2px;
                        
                }
            </style>
            """, unsafe_allow_html=True)


            app = option_menu(
                menu_title='symbiotical.io',
                options=['Home','Dog Parks','Where Am I', 'Weather','Donate','About'],
                icons=['house','signpost-2','compass','cloud-sun','piggy-bank', 'info-circle'],
                menu_icon='person-raised-hand',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
            "icon": {"color": "white", "font-size": "23px"}, 
            "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
            "nav-link-selected": {"background-color": "#4d90fe"},}
            )

            # components.html("<script type='text/javascript' src='https://storage.ko-fi.com/cdn/widget/Widget_2.js'></script><script type='text/javascript'>kofiwidget2.init('Support Me on Ko-fi', '#29abe0', 'W7W6W7JOT');kofiwidget2.draw();</script>", width=200, height=50)
            badge(type="buymeacoffee", name="symbiotical")

        if app == "Home":
            home.app()
        if app == "Donate":
            donate.app()    
        if app == "Dog Parks":
           dog_parks_about.app()  
        if app == "Where Am I":
           where_am_i.app()      
        if app == 'Tech Support':
            tech_support_about.app()
        if app == "Tools":
           tools_about.app() 
        if app == "Weather":
           tools_weather.app() 
        if app == 'About':
            about.app()

        
    
    run()