import os
from io import StringIO 
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


from Dashboard import (load_gemini_pro_model, gemini_pro_vision_response, extract_data_response)


working_directory = os.path.dirname(os.path.abspath(__file__))

#page configration

st.set_page_config(
      page_title= "Ajaj's AI",
      page_icon="brain",
      layout="centered"
)

with st.sidebar:
      selected = option_menu(menu_title="Ajaj's AI",
                             options=['ChatBot','Image Captioning',"Read File"],
                             menu_icon='robot',icons=['chat-dots-fill','image-fill', 'textarea-t','patch-question-fill'], default_index=0)
      

#function role between gemini-pro and streamlit terminology
def translate_role_for_streamlit(user_role):
      if user_role == 'model':
            return "assistant"
      else:
            return user_role
      
if selected == "ChatBot":
      model = load_gemini_pro_model()
      
      #chat hist
      if "chat_session" not in st.session_state:
            st.session_state.chat_session = model.start_chat(history=[])
            
      #streamlit page title
      st.title("ChatBot")
      
      #display chat history
      for message in st.session_state.chat_session.history:
            with st.chat_message(translate_role_for_streamlit(message.role)):
                  st.markdown(message.parts[0].text)
                  
                  
      #input field for user msg
      
      user_prompt = st.chat_input("Ask Gemini-pro")
      
      
      if user_prompt:
            
            st.chat_message('user').markdown(user_prompt)
            with st.spinner('Generating your answer...'):
                  gemini_response = st.session_state.chat_session.send_message(user_prompt) #stream=True
                        
                  # display gemini response
                  # with st.spinner('Searching...'):
                  with st.chat_message("assistant"):
                        st.markdown(gemini_response.text)
            
                  
                  
#image caption

if selected == "Image Captioning":
      #Titie
      st.title("Snap Narrat")
      
      uploaded_image = st.file_uploader("Upload an image...", type=['jpg','jpeg','png'])
      promt = st.text_input("Input:", key="input")
      
      image=""
      if st.button("Generate Caption"):
            if uploaded_image is not None:
                  image = Image.open(uploaded_image)
                  st.image(image, caption="uploaded Image", use_column_width=True)
            response = gemini_pro_vision_response(promt,image)
            st.subheader("The Response is:- ")
            st.write(response)
            
            
            
#Embed Text

if selected == "Read File":
      
      st.title("Extrac the Data From File")

      uploaded_file = st.file_uploader('Upload a file....', type=['pdf','txt','csv'])


      promt = st.text_input('Input: ', key='input')

      if st.button("Get Response"):
            if uploaded_file is not None:
                  file = StringIO(uploaded_file.getvalue().decode("utf-8"))
                  st.file_uploader(file, caption='upload file')
            response = extract_data_response(promt, file)
            st.subheader("The Responce is:- ")
            st.write(response)
      
      #uploading dosc
      
      # input_text = st.text_area(label='', placeholder='Enter you text')
      
      # if st.button("Get Embessings"):
      #       response = embeding_model_response(input_text)
      #       st.markdown(response)