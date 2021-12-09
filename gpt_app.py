import app2
from model_training_service import Code
# from const import API_KEY
import streamlit as st


st.set_page_config(
    page_title="Echo Explain",
    page_icon="🐾",
    layout="centered")

# Pages as key-value pairs
PAGES = {
   "Echo Explain": app2
}

#st.sidebar.title('Go to:')

#selection = st.sidebar.radio("", list(PAGES.keys()))

page = app2

page.app() 
