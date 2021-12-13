from model_training_service import Code
import streamlit as st
from google.oauth2 import service_account
from googleapiclient import discovery

credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        ],
    )
service = discovery.build('sheets', 'v4', credentials=credentials)


def app():
    
    # Creating an object of prediction service
    pred = Code()

    
    # Using the streamlit cache 
    @st.cache
    def process_prompt(input):
        return pred.model_prediction(input=input, api_key=st.secrets.db_key)

    st.image("./ai.png", width=100)
    st.title("ECHO EXPLAIN")
    st.write("---")

    input = st.text_area('Input:')
    global report_text

    if st.button('Submit'):
        st.write('**Output**')
        st.write(f"""---""")
        spreadsheet_id = st.secrets.spreadsheet_id  

        range_ = 'A1' 
             
        with st.spinner(text='In progress'):
            report_text = process_prompt(input)
            #report_text = input [::-1]
            st.markdown(report_text)
            values = [
                (input, report_text)
                    ]
            value_range_body = {
                        'majorDimension' : 'ROWS',
                        'values': values
                    } 

            service.spreadsheets().values().append(
                spreadsheetId=spreadsheet_id, 
                range=range_, 
                valueInputOption='RAW',
                body=value_range_body).execute()
                
    st.write("---")

    st.write("Cordoc LLC. This app will help you understand your echo report using AI. Still in development. Use with caution. Do not use for medical decision making")
       

