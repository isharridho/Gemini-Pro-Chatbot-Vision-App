from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables from .env file

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load gemini pro model and get response
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(prompt):
    # Generate response from the model
    response = model.generate_content(prompt)
    # Count input tokens
    input_token_info = model.count_tokens(prompt)
    input_token_count = input_token_info.total_tokens if hasattr(input_token_info, "total_tokens") else input_token_info["total_tokens"]
    # Count output tokens (response)
    output_token_info = model.count_tokens(response.text)
    output_token_count = output_token_info.total_tokens if hasattr(output_token_info, "total_tokens") else output_token_info["total_tokens"]
    total_tokens = input_token_count + output_token_count
    # Combine response text and token counts
    return (
        f"{response.text}\n\n---\n"
        f"Input tokens: {input_token_count}\n"
        f"Output tokens: {output_token_count}\n"
        f"Total tokens used: {total_tokens}"
    )


# Streamlit app configuration
st.set_page_config(page_title="Gemini Pro Chatbot", page_icon=":robot_face:", layout="wide")
st.title("Gemini Pro Chatbot")
st.write("Ask me anything about Gemini Pro!")

# Input text box for user prompt
user_prompt = st.text_input("Enter your question:", "")

# Button to submit the prompt
if st.button("Submit"):
    if user_prompt:
        with st.spinner("Generating response..."):
            try:
                response = get_gemini_response(user_prompt)
                st.success(response)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question before submitting.")

# Sidebar for additional information
st.sidebar.header("About")          
st.sidebar.write("This is a simple chatbot powered by Google's Gemini Pro model. You can ask it any question, and it will try to provide a helpful response.")
st.sidebar.write("### Instructions")
st.sidebar.write("1. Enter your question in the text box above.\n"
                 "2. Click the 'Submit' button to get a response.\n"
                 "3. If you encounter any issues, please check your API key and internet connection.")

# Sidebar for additional settings
st.sidebar.header("Settings")
st.sidebar.write("You can customize the behavior of the chatbot by modifying the settings below.")
st.sidebar.write("### Model Configuration")
st.sidebar.write("Currently, the model is set to `gemini-2.5-flash-preview-05-20`. You can change it in the code if needed.")

# Sidebar for additional resources
st.sidebar.header("Resources")  
st.sidebar.write("For more information about Google's Gemini Pro, visit the [official documentation](https://developers.google.com/generative-ai/docs/).")


# Footer with contact information
st.markdown("---")
st.markdown("Made with ❤️ by [Isharridho](https://Linkedin.com/in/isharridho)")
