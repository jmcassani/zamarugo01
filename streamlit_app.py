import streamlit as st

# Configuración de la API de OpenAI
openai.api_key = 'sk-proj-9FWmlDJLMjweNyRz8deJT3BlbkFJde76yd3V5BxuGJKdAx6R'  # Reemplaza 'tu_api_key' con tu clave de API de OpenAI

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
