from textblob import TextBlob
import pandas as pd
import streamlit as st

from googletrans import Translator

translator = Translator()

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
        if x >= 0.5:
            st.write( 'Es un sentimiento Positivo 😊')
        elif x <= -0.5:
            st.write( 'Es un sentimiento Negativo 😔')
        else:
            st.write( 'Es un sentimiento Neutral 😐')
