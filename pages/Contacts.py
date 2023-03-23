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
st.header('Contact us')    

st.write(
'''
Team Members:
''')

st.write("[Tom Gheldof](tom.gheldof@kuleuven.be)")
st.write("[Annelore Knoors](annelore.knoors@student.kuleuven.be)")
st.write("[Catarina Arnaud Boleto](catarina.arnaudboleto@student.kuleuven.be)")
st.write("[Fatemehsadat Mirkazemiyan](fatemehsadat.mirkazemiyan@student.kuleuven.be)")
st.write("[Ujjayanta Bhaumik](ujjayanta.bhaumik@kuleuven.be)")
