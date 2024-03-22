import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

import home
import donate
import about

st.set_page_config(
    page_title="Pondering"
)


if "my_input" not in st.session_state:
    st.session_state['my_input'] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)

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
                menu_title='Pondering ',
                options=['Home','Donate','About'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
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
            # if app == "Trending":
            #     trending.app()        
            # if app == 'Your Posts':
            #     your.app()
            if app == 'About':
                about.app()   
    
    run()