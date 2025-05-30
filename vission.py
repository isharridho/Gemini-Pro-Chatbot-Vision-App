from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables from .env file

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load gemini pro model and get response
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(prompt, image):
    default_instruction = "Describe the image in detail."
    if prompt != "":
        response = model.generate_content([image, prompt])
    else:
        response = model.generate_content([image, default_instruction])
    return response.text
    
   
# Streamlit app configuration
st.set_page_config(page_title="Gemini Pro Vision Chatbot", page_icon=":robot_face:", layout="wide")
st.header("Gemini Pro Vision Chatbot")

input=st.text_input("Enter your question:",key="input_text")

# File uploader for image input
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="image_input")
image="" 
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

# Button to submit the prompt
submit = st.button("Submit", key="submit_button")

if submit:
    response=get_gemini_response(input, image)
    st.subheader('the response is:')
    st.write(response)





