import streamlit as st
import streamlit.components.v1 as components
# from dependancies import sign_up, sign_in, fetch_users

st.set_page_config(
    page_title="Dog Parks",
    page_icon="🐶",
    layout='wide'
)

st.title("Dog Parks")

st.image('2puppies.jpg')

st.link_button("Dog Park. Map", "/Dog_Parks._Map")
st.write("A simple map to find local..")
st.write("- Dog Parks (on or off leash)")
st.write("- Pets Stores")
st.write("- Vets")
st.write("- Hospitals")
st.write("")
st.write("If you see a pop-up asking to 'Allow' access, This is so we can discover you current location via GPS or cell towers (less accurate).")
st.write("Whilst you can deny, the functionality of this site will not be as usefull.")



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
# elif st.session_state['authentication_status'] == False:
#     st.error('Username/password is incorrect')
#     sign_in()
# elif st.session_state['authentication_status'] == None:
#     st.warning('Please enter your username and password')
#     sign_in()
#     #sign_up()