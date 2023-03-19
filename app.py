import streamlit as st
from PIL import Image
import random


st.header('Timeline of Posters')

st.write(
        f'<iframe class="responsive-iframe" src="https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=1-QPh9s5fmE4Pc_2OVBzOProVPq9k5-E1Er2srsaPbCU&font=Default&lang=en&initial_zoom=2" width="900" height="600"></iframe>',
        unsafe_allow_html=True,
    )
    
st.header('Generated Posters')    
st.write('An AI model has been created to generate World War posters. The training dataset was provided by KU Leuven. Press the button to generate a poster.')
imageList = ['1.png','2.png','3.png']

image = Image.open(random.choice(imageList))
if st.button('Generate'):
    st.image(image, caption='Generated posters')