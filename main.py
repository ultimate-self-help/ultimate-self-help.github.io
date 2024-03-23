import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

import home
import templates.dog_parks_about as dog_parks_about
import templates.donate as donate
import templates.about as about
import templates.tools_about as tools_about
import templates.tech_support_about as tech_support_about

st.set_page_config(
    page_title="Ultimate-Self-Help",
    page_icon="🐶",
    layout='wide'
)

# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)

if "my_input" not in st.session_state:
    st.session_state['my_input'] = ""

# my_input = st.text_input("Input a text here", st.session_state["my_input"])
# submit = st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You have entered: ", my_input)

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
            app = option_menu(
                menu_title='Welcome ',
                options=['Home','Dog Parks','Tech Support','Tools','Donate','About'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill', 'house-fill','person-circle','trophy-fill'],
                menu_icon='chat-text-fill',
                default_index=2,
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
        if app == 'About':
            about.app()   
    
    run()