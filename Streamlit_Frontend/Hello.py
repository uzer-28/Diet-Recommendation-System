import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Diet Recommendation System! 👋")

st.sidebar.success("Select a recommendation way.")

st.markdown(
    """
    <div style="text-align: center;">
        A diet recommendation web application using content-based approach with Scikit-Learn, FastAPI and Streamlit.
        <br><br>
        Submitted by:
        <br><br>
        <b>UZER QAZI</b>  
        <br>
        <b>HARIS JIRATI</b>  
        <br>
        <b>HANNAN MUNDEWADI</b>
        <br><br>
        Under the guidance of
        <br><br>
        <b>DR. M.H.NAIKWADI</b>
    </div>
    """, unsafe_allow_html=True
)
