import streamlit as st
import os
from langchain import PromptTemplate
from langchain_openai import OpenAI

#Input OpenAI API Key
st.markdown("## Enter Your OpenAI API Key")

def get_openai_api_key():
    input_text = st.text_input(label="OpenAI API Key ",  placeholder="Ex: sk-2twmA8tfCb8un4...", key="openai_api_key_input", type="password")
    return input_text

openai_api_key = get_openai_api_key()

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
