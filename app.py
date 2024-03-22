import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
# import * from sidebar-left
# STREAMLIT HOME PAGE: https://docs.streamlit.io/library/api-reference#magic-commands

st.set_page_config(
    page_title="Ultimate-Self-Help",
    page_icon="👋",
    layout='wide'
)

if "my_input" not in st.session_state:
    st.session_state['my_input'] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# https://www.youtube.com/watch?v=hEPoto5xp3k
with st.sidebar:
    selected = option_menu(
        #menu_title="Main Menu", #required.
        menu_title=None, #required
        #menu_icon="cast",
        options=["Home", "Dog Parks", "Tech Support", "Tools","About", "Donate"],
        icons=['house', 'book', 'envelope', 'book', 'book', 'book'],
        default_index=0

    )


#st.title(f"You selected: {selected}" )
# if selected == "Home":
#     pass
# if selected == "Dog Parks":
#     st.page_link(page="pages/dog-parks-about.py", label="Dog Parks")
# if selected == "Tech Support":
#     st.page_link(page="pages/tech-support-about.py", label="Tehc Support")
# if selected == "Tools":
#     st.page_link(page="pages/tools-about.py", label="Tools")
# if selected == "About":
#     st.page_link(page="pages/about.py", label="About")
# if selected == "Donate":
#     st.page_link(page="pages/donate.py", label="Donate")

if selected == "Home":
    pass
if selected == "Dog Parks":
    switch_page("dog-parks-about")
if selected == "Tech Support":
    switch_page("tech-support-about")
#     st.page_link(page="pages/tech-support-about.py", label="Tehc Support")
if selected == "Tools":
    switch_page("tools-about")    
#     st.page_link(page="pages/tools-about.py", label="Tools")
if selected == "About":
    switch_page("about")   
#     st.page_link(page="pages/about.py", label="About")
if selected == "Donate":
    switch_page("donate")   
#     st.page_link(page="pages/donate.py", label="Donate")


# with st.container():
#     st.write("---")
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.header("Link")
#         st.page_link("pages/dog-parks-map.py", label="Dog Parks. Map")        


#     with right_column:
#         st.header("Description")
#         st.write(
#             """
#             Find local dog parks, pet stores, vets and hospitals.
#             """
#         )

st.write("---")
st.write("Donate (One off)")
st.write("Donate as little or as much as you like. To keep this site online.")
st.write("The more donations I recieve, the more features I can add for you..")

components.html('<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="ultimateselfhelp" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>')



# st.sidebar.success("Select a page above.")

# Global state (all pages)
# Source: https://www.youtube.com/watch?v=YClmpnpszq8&list=PL7QI8ORyVSCaejt2LICRQtOTwmPiwKO2n&index=14
# if "my_input" not in st.session_state:
#     st.session_state["my_input"] = ""

# my_input = st.text_input("Input a text here", st.session_state["my_input"])
# submit = st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You have entered: ", my_input)

