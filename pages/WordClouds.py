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
  
  
  
st.title("Topic Modelling")
st.header('Wordclouds')    
st.write('There are two types of documents: news publications vs regulations​. Some observations:')
st.write('Always Dutch, French and German for news (mass media communication)​. For news publications: war vocabulary, time ("gisteren"), place, news vocabulary. For regulations​: juridical lexicon, syntaxis related to orders, daily life lexicon ("boter"), war vocabulary​')
imageList = ['1.png','2.png','3.png']

image = Image.open('titles.png')
image2 = Image.open('fullText.png')
if st.button('Generate Wordcloud of Original Title texts:'):
    st.image(image, caption=' Wordcloud of Original titles')
    
if st.button('Generate Wordcloud of Full text of the original texts:'):
    st.image(image2, caption='Full text of the original texts ')   

if st.button('Generate Wordcloud by year:'):
    st.image('1914.png', caption='Wordcloud by years')

if st.button('Generate Wordcloud by titles of orders and regulations:'):
    st.image('orders.png', caption='Titles of orders and regulations')

if st.button('Generate Wordcloud by texts of news publications:'):
    st.image('news.png', caption='Texts of news publications')    
