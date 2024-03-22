import streamlit as st

button1 = st.button("Clean text.")
text1 = st.text_area("Paste in here..")
# text2 = st.text_area("Result")

def clean_text(text1):
    cleaned_text = text1.replace("`", "").replace("-\n", "").replace("\n\n", "&&***&&").replace("\n", "").replace("&&***&&", "\n\n").strip()
    return cleaned_text

if button1:
    #st.write(text)
    col1, col2 = st.columns(2)
    col1_expander = col1.expander("Expand Original")

    with col1_expander:
        col1_expander.header("Original Text")
        col1_expander.write(text1)

    col2_expander = col2.expander("Expand Cleaned")
    with col2_expander:
        col2.header("Cleaned Text")
        clean = clean_text(text1) # Clean text from function.
        col2_expander.write(clean)