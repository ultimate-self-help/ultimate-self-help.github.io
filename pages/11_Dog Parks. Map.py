import streamlit as st
import streamlit.components.v1 as components
# import streamlit_authenticator as stauth
# from dependancies import sign_up, sign_in, fetch_users

st.set_page_config(
    page_title="Dog Parks. Map",
    page_icon="👋",
    layout='wide'
)

HtmlFile = open("pet-friendly.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
components.html(source_code, height=900, scrolling=False)

# def initialize_session_state():
#     if 'name' not in st.session_state:
#         st.session_state['name'] = None
#     if 'authentication_status' not in st.session_state:
#         st.session_state['authentication_status'] = None
#     if 'username' not in st.session_state:
#         st.session_state['username'] = None

# initialize_session_state()

# if st.session_state['authentication_status']:
#     st.write('Welcome *%s*' % (st.session_state['name']))
#     st.title('Some content')
#     HtmlFile = open("pet-friendly.html", 'r', encoding='utf-8')
#     source_code = HtmlFile.read()
#     components.html(source_code, height=900, scrolling=False)
# elif st.session_state['authentication_status'] == False:
#     st.error('Username/password is incorrect')
#     sign_in()
# elif st.session_state['authentication_status'] == None:
#     st.warning('Please enter your username and password')
#     sign_in()