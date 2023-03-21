import streamlit as st
from PIL import Image
import random
  
st.title("Generate Wartime Posters")
st.header('Generated Posters')    
st.write('An AI model has been created to generate World War posters. The training dataset was provided by KU Leuven. Press the button to generate a poster.')
imageList = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png']

image = Image.open(random.choice(imageList))
if st.button('Generate'):
    st.image(image, caption='Generated posters')
