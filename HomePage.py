import streamlit as st
from PIL import Image
import random

st.header('ChaoTech Warriors')

st.write(
'''
Wartime poster dataset.

We are team 4 participating in the KU Leuven BiblioTech 2023 Hackathon. Our dataset has multilingual wartime posters with proclamations issued by the German General Goverment in Belgium during World War I.


We created an interface that allows interested people to discover these posters in an easier way. We want to create a timeline, with a selection of the posters, as well as a geographical map on which the posters are displayed. For the timeline, we want to use TimelineJS.  

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


    
    
