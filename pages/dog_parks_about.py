import streamlit as st
import streamlit.components.v1 as components
# from dependancies import sign_up, sign_in, fetch_users
from images import *
def app():

    st.title("Dog Parks")
    
    with st.expander("Help"):
        col1, col2, col3 = st.columns(3)
        with col2:
            st.image('images/2puppies.jpg')
        #st.page_link("dogparks2.py", icon="🐶", label="DogParks2")
        # st.page_link("dog_parks_map.py", label="Dog Park. Map", icon="🐶")
        st.write("A simple map to find local..")
        st.write("- Dog Parks (on or off leash)")
        st.write("- Pets Stores")
        st.write("- Vets")
        st.write("- Hospitals")
        st.write("")

        st.markdown('## How To Use:')
        st.write("1. Once you can see the map, suggest to hide this site left sidebar / menu. (Optional)")
        st.write("2. Confirm you selected 'allow' permissions, see below.")        
        st.write("3. Once map appears, confirm it has detected you in correct location i.e Country / town.")
        st.write("4. Select one of the top menu on map.")
        st.write("5. Select 'Full Screen' mode from top right of map (Optional)")

        st.markdown('## My Locations Is Not Correct:')
        st.write("1. You must be withing cell / mobile tower range i.e. have a cell or mobile signal.")
        st.write("2. You must 'allow' this site access via the initial pop-up.")
        st.write("3. For best accuracy, you must enable GPS / 'Location' tracking from withing your mobile device 'settings'.")

        st.write("Warning: Data accuracy can not be garanteed")
        st.write("The source data is from public entering into google.com.")
        st.write("It may not be accurate i.e. Old information incorrect labeling of 'off-leash' etc.")

        st.subheader("FAQ")
        st.write("Can I add or update an entry?")
        st.write("Currently this can only be done via google.com")



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
    # elif st.session_state['authentication_status'] == False:
    #     st.error('Username/password is incorrect')
    #     sign_in()
    # elif st.session_state['authentication_status'] == None:
    #     st.warning('Please enter your username and password')
    #     sign_in()
    #     #sign_up()