from textblob import TextBlob
import pandas as pd
import numpy as np
import streamlit as st
from googletrans import Translator
from gtts import gTTS
#from IPython.display import Audio
import random
from random import choice
##import openai

col1, col2 = st.columns(spec=[0.7, 0.3], gap="medium")
translator = Translator()
flag = 0
frases_motivacionales = [
    "La determinación es la clave del éxito.",
    "La perseverancia supera cualquier obstáculo.",
    "Cada día es una oportunidad para crecer y mejorar.",
    "La pasión por lo que haces marca la diferencia.",
    "El camino hacia el éxito está lleno de desafíos, ¡Tú puedes superarlos!",
    "Eres lo mejor en lo que haces, confía en tu proceso",
    "El éxito es el resultado de la perseverancia y la determinación.",
    "Cada día es una nueva oportunidad para alcanzar tus metas.",
    "El camino hacia tus sueños puede ser difícil, pero vale la pena recorrerlo.",
    "No temas cometer errores; son lecciones que te acercan al éxito.",
    "La pasión y el esfuerzo son la clave para lograr tus objetivos.",
    "Nunca subestimes el poder de una mente positiva.",
    "El progreso se logra dando un paso a la vez.",
    "Tu actitud determina tu altitud en la vida.",
    "La confianza en ti mismo es el primer paso hacia el éxito.",
    "No importa cuán difícil sea el camino, siempre hay una forma de avanzar.",
]


#sObjetivo = list() #sentimiesnto objetivizados por la formula polarity*subjetivity
##Seteando IA
##openai.api_key = st.secrets["OPENAI_API_KEY"]
##if "openai_model" not in st.session_state:
    ##st.session_state["openai_model"] = "gpt-3.5-turbo"
def texto_a_voz(texto, nombre_archivo):
    tts = gTTS(texto, lang='es', tld='com.mx')
    tts.save(nombre_archivo)

with col1:
    st.header('SerenIA')
    st.caption ("Bot emocional")
    st.write("Este bot analiza por medio de IA la carga emocional de tu respuesta, con base en ello, genera respuestas afines para crear un hábito de pensamientos positivos")


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
            st.caption("Recuerda...")

            if x >= 0.3:
                st.write( 'Es un sentimiento Positivo 😊')
                texto_a_voz('Es un sentimiento Positivo', 'respuesta.mp3')
                st.audio('respuesta.mp3', format='audio/mp3')
            elif x <= -0.2:
                st.write(frases_motivacionales[iFrase])
                texto_a_voz(frases_motivacionales[iFrase], 'respuesta.mp3')
                st.audio('respuesta.mp3', format='audio/mp3')
            else:
                st.write('Si necesitas ayuda, no dudes en pedirla. Estoy para escucharte si me dices un poco más')
                texto_a_voz('Si necesitas ayuda, no dudes en pedirla. Estoy para escucharte si me dices un poco más', 'respuesta.mp3')
                st.audio('respuesta.mp3', format='audio/mp3')

with col2:
    st.title("Frase felíz 😊")
    button_press = st.button("Generar")
    
    if (button_press == True):
        st.write(choice(frases_motivacionales))
        



