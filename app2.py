from model_training_service import Code
#from const import API_KEY
import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect


def app():
        
    # Creating an object of prediction service
    pred = Code()

  # api_key = st.sidebar.text_input("OpenAI API Key:", type="password")

    # Using the streamlit cache 
    @st.cache
    def process_prompt(input):
        return pred.model_prediction(input=input, api_key=st.secrets.db_key)
    
            
        # Setting up the Title
          
    st.title("Echo explain")
    st.header("Powered by Cordoc LLC") 

    st.write(f"""
        ## Made by Cordoc LLC
        """)
    st.write("This app will help you understand your echo report using AI")
        
    st.write("---")

    st.write(f"""
       Still in development. Use with caution. Do not use to medical medical decisions📖
        """)

    st.write(f"""---""")

    st.image("./ai.png", use_column_width=True)

    input = st.text_input('Input:')

    if st.button('Submit'):
        st.write('**Output**')
        st.write(f"""---""")
        with st.spinner(text='In progress'):
            report_text = process_prompt(input)
            st.markdown(report_text)
   # else:
    #    st.error("🔑 API Key Not Found!")
   #     st.info("💡 Copy paste your OpenAI API key that you can find in User -> API Keys section once you log in to the OpenAI API Playground")

   # Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets.gcp_service_account,
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

sheet_url = st.secrets.private_gsheets_url
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")