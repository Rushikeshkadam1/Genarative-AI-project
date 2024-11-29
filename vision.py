from dotenv import load_dotenv
load_dotenv() # to load all enviroment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##  function to load Gemini pro models and get response
model=genai.GenerativeModel("gemini-1.5-flash-latest")
def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response=model.generate_content(image)
    return response.text
    

# Initialize our Streamlit app

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Image Application")

input=st.text_input("Input Prompt: ", key="input")

# we need to give image upload option to user

uploaded_file = st.file_uploader("Choose an image to upload--->", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit = st.button("Get response")

# if submit is clicked
if submit:
    response = get_gemini_response(input, image)
    st.subheader("THe response is")
    st.write(response)