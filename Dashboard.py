from dotenv import load_dotenv
load_dotenv()

# import streamlit as st

import os
import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load gemini for chatbot
chatbot_model = genai.GenerativeModel("gemini-pro")
def load_gemini_pro_model():
      return chatbot_model


#function for image captioning
image_model = genai.GenerativeModel("gemini-1.5-flash")

def gemini_pro_vision_response(promt, image):
      if promt!='':
            response=image_model.generate_content([promt, image])
      else:
            response=image_model.generate_content(image)
      return response.text
      
      
      
      
#function for extract data form Text file

file_model = genai.GenerativeModel("gemini-1.5-flash")
def extract_data_response(promt, file):
      
      if promt!='':
           response = file_model.generate_content([promt, file])
      else:
            response = file_model.generate_content([file])
      return response.text    
  
