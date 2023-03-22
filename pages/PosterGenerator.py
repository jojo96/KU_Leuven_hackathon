import streamlit as st
from PIL import Image
import random

import base64
  
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg.png') #  
  
st.title("Generate Wartime Posters")
st.header('Generated Posters')    
st.write('An AI model has been created to generate World War posters. The training dataset was provided by KU Leuven. Press the button to generate a poster.')
imageList = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png']

image = Image.open(random.choice(imageList))
if st.button('Generate'):
    st.image(image, caption='Generated posters')
