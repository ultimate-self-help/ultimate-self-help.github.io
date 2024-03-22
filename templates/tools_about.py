import streamlit as st

def app():
    st.write("Tools")

    # with st.container():
    #     st.write("---")
    #     left_column, right_column = st.columns(2)
    #     with left_column:
    #         st.header("Link")
    #         st.page_link("pages/tools_clean_text.py", label="Clean Text")        
        
    #     with right_column:
    #         st.header("Description")
    #         st.write(
    #             """
    #             Remove 'wierd charactors' from text e.g. carriage returns.
    #             """
    #         )





    st.write("Paste your / any text in the next box below, then select 'Clean Text' button.")
    st.write("Will remove 'wierd characters' like carriage returns etc.")
    text1 = st.text_area("Paste in here..")
    button1 = st.button("Clean Text Now")
    # text2 = st.text_area("Result")

    def clean_text(text1):
        cleaned_text = text1.replace("`", "").replace("-\n", "").replace("\n\n", "&&***&&").replace("\n", "").replace("&&***&&", "\n\n").strip()
        return cleaned_text

    if button1:
        #st.write(text)
        col1, col2 = st.columns(2)
        col1_expander = col1.expander("Expand Original")

        with col1_expander:
            #col1_expander.header("Original Text")
            col1_expander.write(text1)

        col2_expander = col2.expander("Expand Cleaned")
        with col2_expander:
            #col2.header("Cleaned Text")
            clean = clean_text(text1) # Clean text from function.
            col2_expander.write(clean)
