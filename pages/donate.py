import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.buy_me_a_coffee import button
from streamlit_extras.badges import badge
from images import *
from PIL import Image

def app():

    # components.html('<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="ultimateselfhelp" data-color="#FFDD00" data-emoji="☕"  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>')


    with st.container():
        colL, colM, colR = st.columns(3)

        with colM:
            st.write("Donate as little or as much as you like. To keep this site online.")
            st.write("The more donations I recieve, the more features I can add for you..")

             # VERSION 2.
            button(username="ultimateselfhelp", floating=False, width=221, emoji="😀")
            
            st.image("images/ush_bmc_qrcode.png", width=200)

            st.write("Thanks in advanced! 😁")

        #VERSION 1
        # components.html('<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="ultimateselfhelp" data-color="#FFDD00" data-emoji="☕"  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>')
        
        # ush_bmc_qrcode = Image.open('ush_bmc_qrcode.png')
        # resized_image = ush_bmc_qrcode.resize((200, 200))
        # st.image(resized_image)    

    with st.sidebar:
        badge(type="buymeacoffee", name="ultimateselfhelp")
        #button(username="ultimateselfhelp", floating=False, width=221, emoji="😀")
