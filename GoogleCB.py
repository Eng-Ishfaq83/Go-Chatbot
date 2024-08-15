import streamlit as st
import google.generativeai as genai

import os

#Configure the API Key

genai.configure(api_key=os.environ["Google_API_Key"])

# Initiate Generative Model
# Model = genai.generative('gemini-pro')

model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get response from Model
def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit Interface

st.title("🚌 Simple Chatbot 🚌")
st.write("Powered by Google Generative AI")

if "history" not in st.session_state:
    st.session_state["history"] = []


# user_input = input("Enter your Prompt = ")
# output = get_chatbot_response(user_input)
# print(output)

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2500)
    submit_button = st.form_submit_button("GO")

    if submit_button:
        if user_input:
            response = get_chatbot_response(user_input)
            st.session_state.history.append((user_input, response))
        else:
            st.warning("Please Enter a Prompt")


            