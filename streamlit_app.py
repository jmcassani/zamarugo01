import streamlit as st
import os
from langchain import PromptTemplate
from langchain_openai import OpenAI

# Acceder a la clave de API desde la variable de entorno
api_key = os.getenv("OPENAI_API_KEY")

# Configurar la clave de API
openai.api_key = api_key

def generate_response(question):
    prompt = "Pregunta: {}\nRespuesta:".format(question)
    response = openai.Completion.create(
        engine="text-davinci-003",  # Puedes cambiar el motor según tus necesidades
        prompt=prompt,
        temperature=0.5,
        max_tokens=150
    )
    return response.choices[0].text.strip()


# Interfaz de usuario
st.title("Chatbot de Coches")
question = st.text_input("Haz una pregunta sobre coches")

if st.button("Enviar"):
    if question:
        response = generate_response(question)
        st.text(response)
    else:
        st.warning("Por favor, introduce una pregunta")
