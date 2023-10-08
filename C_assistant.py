from textblob import TextBlob
import pandas as pd
import numpy as np
import streamlit as st
from googletrans import Translator
##import openai

translator = Translator()
##Seteando IA
##openai.api_key = st.secrets["OPENAI_API_KEY"]
##if "openai_model" not in st.session_state:
    ##st.session_state["openai_model"] = "gpt-3.5-turbo"

st.header('HOW U DOING (bot)')

with st.chat_message("user"):
    st.write("¡Hola!, ¿Cómo estuvo tu día? 👋")

with st.expander('Escribe aquí'):
    text = st.text_input('')
    if text:
        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        polaridades = []
        polaridades.apppend(x)
        
        if x >= 0.5:
            st.write( 'Es un sentimiento Positivo 😊')
        elif x <= -0.5:
            st.write( 'Es un sentimiento Negativo 😔')
        else:
            st.write( 'Es un sentimiento Neutral 😐')

hist_values = np.histogram(polaridades, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
        
