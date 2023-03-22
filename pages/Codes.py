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
  
st.title("Codes")
st.header('Link to Github repository')    
st.write('You can find the codes related to our project in our GitHub repository.')

st.write(
'''
You can find the code for: 

- Wordcloud generator

- Language Separator

- Automatic translator

and so on..
''')

st.write("[Link to repo](https://github.com/jojo96/team4KUL)")