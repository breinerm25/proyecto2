from textblob import TextBlob
import pandas as pd
import numpy as np
import streamlit as st
from googletrans import Translator
from gtts import gTTS
#from IPython.display import Audio
import random
##import openai

translator = Translator()
frases_motivacionales = [
    "La determinación es la clave del éxito.",
    "La perseverancia supera cualquier obstáculo.",
    "Cada día es una oportunidad para crecer y mejorar.",
    "La pasión por lo que haces marca la diferencia.",
    "El camino hacia el éxito está lleno de desafíos, ¡Tú puedes superarlos!",
    "Eres lo mejor en lo que haces, confía en tu proceso",
]
#sObjetivo = list() #sentimiesnto objetivizados por la formula polarity*subjetivity
##Seteando IA
##openai.api_key = st.secrets["OPENAI_API_KEY"]
##if "openai_model" not in st.session_state:
    ##st.session_state["openai_model"] = "gpt-3.5-turbo"

st.header('HOW U DOING (bot)')



with st.chat_message("user"):
    st.write("¡Hola!, ¿Cómo te sientes hoy? 👋")

with st.expander('Escribe aquí'):
    text = st.text_input('')
    if text:
        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x= (round(blob.sentiment.polarity,2) / round(blob.sentiment.subjectivity,2))
        st.write(x)
        #sObjetivo.apppend(x)
        iFrase = random.randint(0, len(frases_motivacionales) - 1)

        if x >= 0.5:
            st.write( 'Es un sentimiento Positivo 😊')
        elif x <= -0.5:
            st.write(frases_motivacionales[iFrase])
        else:
            st.write('Si necesitas ayuda, no dudes en pedirla. Estoy para escucharte si me dices un poco más')

       
