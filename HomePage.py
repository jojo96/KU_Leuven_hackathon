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

st.header('ChaoTech Warriors')

st.write(
'''
Wartime poster dataset.

We are team 4 participating in the KU Leuven BiblioTech 2023 Hackathon. Our dataset has multilingual wartime posters with proclamations issued by the German General Goverment in Belgium during World War I.


We created an interface that allows interested people to discover these posters in an easier way. We created a timeline, with a selection of the posters using TimelineJS.  
You can form an understanding of the content as we did Topic Modelling, separated the posters to identifiable categories, and created Word Clouds.

''')


st.header('Timeline of Posters')


st.write("[Try our interactive timeline](https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=1-QPh9s5fmE4Pc_2OVBzOProVPq9k5-E1Er2srsaPbCU&font=Default&lang=en&initial_zoom=2)")


st.write(
'''
We did topic modelling on the wartime posters to categorize our results according to different features of the posters, such as year of publication, location, etc... You can check the sidebar for trying out the wordclouds.

Also, we created a generator that can create new wartime posters based on an analysis of the old ones. Check the sidebar for this feature.

'''
)

st.header('Our team')


st.write(
'''

Participants:

	
• Emanuele Caminada   •Ujjayanta Bhaumik • Benneth Paredis • Annelore Knoors
	
• Tem Mirkazemiyan • Juliet van Rosendaal • Catarina Boleto • Patrick Sy

Team Leader:

- Tom Gheldof
'''
)


    
    
