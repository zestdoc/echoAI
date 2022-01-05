import app2
from model_training_service import Code
# from const import API_KEY
import streamlit as st


st.set_page_config(
    page_title="Echo NLP",
    page_icon=":heart:",
    layout="centered",
    menu_items={
         'Get Help': 'https://www.cordoc.com/help',
         'Report a bug': "https://www.cordoc.com/bug",
         'About': "# Cordoc LLC.  THIS WEBSITE DOES NOT PROVIDE MEDICAL ADVICE. It is intended for informational purposes only. It is not a substitute for professional medical advice, diagnosis or treatment. Never ignore professional medical advice in seeking treatment because of something you have read on this  website. If you think you may have a medical emergency, immediately call your doctor or dial 911. "
     })

# Pages as key-value pairs
PAGES = {
   "Echo NLP": app2
}

#st.sidebar.title('Go to:')

#selection = st.sidebar.radio("", list(PAGES.keys()))

page = app2

page.app() 
