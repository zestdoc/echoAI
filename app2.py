from model_training_service import Code
import streamlit as st
from google.oauth2 import service_account
from googleapiclient import discovery
import requests


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

    st.image("./ai.png")
    
    desired_text = 'default_training'
    jargon_summary = 'default_jargon_summary'
    input = st.text_area('Paste echo report conclusion here:')
    training = st.checkbox('Add this to traning data?')
    translate = st.checkbox('Translate result from English to preferred language')
    if training:
                desired_text = st.text_area('Simplified text:')
                jargon_summary = st.text_area ('Jargon summary')
    

   

    Languages = {'afrikaans':'af','albanian':'sq','amharic':'am','arabic':'ar','armenian':'hy','azerbaijani':'az','basque':'eu','belarusian':'be','bengali':'bn','bosnian':'bs','bulgarian':'bg','catalan':'ca','cebuano':'ceb','chichewa':'ny','chinese (simplified)':'zh-cn','chinese (traditional)':'zh-tw','corsican':'co','croatian':'hr','czech':'cs','danish':'da','dutch':'nl','english':'en','esperanto':'eo','estonian':'et','filipino':'tl','finnish':'fi','french':'fr','frisian':'fy','galician':'gl','georgian':'ka','german':'de','greek':'el','gujarati':'gu','haitian creole':'ht','hausa':'ha','hawaiian':'haw','hebrew':'iw','hebrew':'he','hindi':'hi','hmong':'hmn','hungarian':'hu','icelandic':'is','igbo':'ig','indonesian':'id','irish':'ga','italian':'it','japanese':'ja','javanese':'jw','kannada':'kn','kazakh':'kk','khmer':'km','korean':'ko','kurdish (kurmanji)':'ku','kyrgyz':'ky','lao':'lo','latin':'la','latvian':'lv','lithuanian':'lt','luxembourgish':'lb','macedonian':'mk','malagasy':'mg','malay':'ms','malayalam':'ml','maltese':'mt','maori':'mi','marathi':'mr','mongolian':'mn','myanmar (burmese)':'my','nepali':'ne','norwegian':'no','odia':'or','pashto':'ps','persian':'fa','polish':'pl','portuguese':'pt','punjabi':'pa','romanian':'ro','russian':'ru','samoan':'sm','scots gaelic':'gd','serbian':'sr','sesotho':'st','shona':'sn','sindhi':'sd','sinhala':'si','slovak':'sk','slovenian':'sl','somali':'so','spanish':'es','sundanese':'su','swahili':'sw','swedish':'sv','tajik':'tg','tamil':'ta','telugu':'te','thai':'th','turkish':'tr','turkmen':'tk','ukrainian':'uk','urdu':'ur','uyghur':'ug','uzbek':'uz','vietnamese':'vi','welsh':'cy','xhosa':'xh','yiddish':'yi','yoruba':'yo','zulu':'zu'}

    if translate:
     targetLanguage = st.selectbox('Output language',
                       ('marathi','malayalam', 'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'turkmen', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu'))
     targetLang = Languages [targetLanguage]
    else:
      targetLang = 'en'   

    global report_text 

    if st.button('Submit'):
        st.header('Simplified echo report')
        spreadsheet_id = st.secrets.spreadsheet_id  

        range_ = 'A1' 
             
        with st.spinner(text='In progress'):
            report_text = process_prompt(input)
            # report_text = 'default12345'
            st.success(report_text)
            values = [
                (input, report_text, desired_text, jargon_summary)
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
            
# sourceLang = st.text_input("Enter source language:")
            sourceLang = "en"
            sourceText = report_text
            url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=" + sourceLang + "&tl=" + targetLang + "&dt=t&q=" + sourceText
            response = requests.get(url)
            #if st.button('Translate'):
            result = response.text
            indexx = result.index('","')
            result = result[4:int(indexx)]
  # st.write(result)
            if translate:
                st.header(targetLanguage)
                st.success(result)
            
                
    st.write("---")
