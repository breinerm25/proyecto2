from textblob import TextBlob
import pandas as pd
import numpy as np
import streamlit as st
from googletrans import Translator
from gtts import gTTS
#from IPython.display import Audio
import random
##import openai

col1, col2 = st.columns(spec=[0.7, 0.3], gap="medium")
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
st.write("Este bot analiza por medio de IA la carga emocional de tu respuesta, con base en ello, genera respuestas afines para crear un hábito de pensamientos positivos")

with col1:
    with st.chat_message("user"):
        st.write("¡Hola!, ¿Cómo te sientes hoy? 👋")

    
    with st.expander('Escribe aquí'):
        text = st.text_input('')
        if text:
            translation = translator.translate(text, src="es", dest="en")
            trans_text = translation.text
            blob = TextBlob(trans_text)
            x= round(round(blob.sentiment.polarity,2) / (blob.sentiment.subjectivity+0.001),2)
            st.write("Tú respuesta corresponde a: " , x , "puntos")
            
            #sObjetivo.apppend(x)
            iFrase = random.randint(0, len(frases_motivacionales) - 1)
            st.write("Frases diaria")

            if x >= 0.3:
                st.write( 'Es un sentimiento Positivo 😊')
            elif x <= -0.2:
                st.write(frases_motivacionales[iFrase])
            else:
                st.write('Si necesitas ayuda, no dudes en pedirla. Estoy para escucharte si me dices un poco más')

        
with col2:
    st.title("ZONA NUEVA")




