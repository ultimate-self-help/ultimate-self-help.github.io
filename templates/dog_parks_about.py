import streamlit as st
import streamlit.components.v1 as components
# from dependancies import sign_up, sign_in, fetch_users
def app():

    st.title("Dog Parks")
    
    with st.expander("Dog Park. Help"):
        st.image('2puppies.jpg')
        #st.page_link("dogparks2.py", icon="🐶", label="DogParks2")
        # st.page_link("dog_parks_map.py", label="Dog Park. Map", icon="🐶")
        st.write("A simple map to find local..")
        st.write("- Dog Parks (on or off leash)")
        st.write("- Pets Stores")
        st.write("- Vets")
        st.write("- Hospitals")
        st.write("")
        st.write("If you see a pop-up asking to 'Allow' access, This is so we can discover you current location via GPS or cell towers (less accurate).")
        st.write("Whilst you can deny, the functionality of this site will not be as usefull.")

        st.write("Use the top right icon within the map to expand full screen.")


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