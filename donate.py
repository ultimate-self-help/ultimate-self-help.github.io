import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

def app():
    st.write("Donate as little or as much as you like. To keep this site online.")
    st.write("The more donations I recieve, the more features I can add for you..")

    # components.html('<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="ultimateselfhelp" data-color="#FFDD00" data-emoji="☕"  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>')


    with st.container():
        #left_column, right_column = st.columns(2)
        # with left_column:
        #     components.html('<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="ultimateselfhelp" data-color="#FFDD00" data-emoji="☕"  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>')
        # with right_column:
        #     ush_bmc_qrcode = Image.open('ush_bmc_qrcode.png')
        #     resized_image = ush_bmc_qrcode.resize((200, 200))
        #     st.image(resized_image)
            ### st.image('ush_bmc_qrcode.png', width=None).resize((600, 400))

        components.html('<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="ultimateselfhelp" data-color="#FFDD00" data-emoji="☕"  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>')
        
        # ush_bmc_qrcode = Image.open('ush_bmc_qrcode.png')
        # resized_image = ush_bmc_qrcode.resize((200, 200))
        # st.image(resized_image)    
        st.image("ush_bmc_qrcode.png", width=200)

    st.write("Thanks in advanced! 😁")

    #by_me_coffe_html = '<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="ultimateselfhelp" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>'
    #st.markdown(by_me_coffe_html, unsafe_allow_html=True)
    #st.markdown(by_me_coffe_html, unsafe_allow_html=False)