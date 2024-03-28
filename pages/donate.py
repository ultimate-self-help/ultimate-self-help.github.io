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

        with colL:
            pass

        with colM:
            st.write("Donate as little or as much as you like to keep this site online.")
            st.write("The more donations recieved, the more features can be added for you..")

             # VERSION 2.
            #button(username="ultimateselfhelp", floating=False, width=221, emoji="😀")
            #st.html("<script type='text/javascript' src='https://storage.ko-fi.com/cdn/widget/Widget_2.js'></script><script type='text/javascript'>kofiwidget2.init('Support Me on Ko-fi', '#29abe0', 'W7W6W7JOT');kofiwidget2.draw();</script> ")
            # components.html("<script type='text/javascript' src='https://storage.ko-fi.com/cdn/widget/Widget_2.js'></script><script type='text/javascript'>kofiwidget2.init('Support Me on Ko-fi', '#29abe0', 'W7W6W7JOT');kofiwidget2.draw();</script>", width=200, height=55)
                 
            #st.image("images/ush_bmc_qrcode.png", width=200)
            # st.image("images/kofi-qrcode.png", width=200)
            badge(type="buymeacoffee", name="symbiotical")
            
            st.image("images/symbiotical.io_bmc_qrcode.png", width=200)

            st.write("Thanks in advanced! 😁")

        with colR:
            pass

        #VERSION 1
        # components.html('<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="ultimateselfhelp" data-color="#FFDD00" data-emoji="☕"  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>')
        
        # ush_bmc_qrcode = Image.open('ush_bmc_qrcode.png')
        # resized_image = ush_bmc_qrcode.resize((200, 200))
        # st.image(resized_image)    

        #badge(type="buymeacoffee", name="ultimateselfhelp")
        #badge(type="kofi", name="symbiotical")
        #button(username="ultimateselfhelp", floating=False, width=221, emoji="😀")
        