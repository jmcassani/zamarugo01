import streamlit as st
import openai

# Configura tu API key de OpenAI
openai.api_key = "sk-proj-9FWmlDJLMjweNyRz8deJT3BlbkFJde76yd3V5BxuGJKdAx6R"

def chat_ui():
    st.title("Chatbot de Automoción")

    # Recibe la pregunta del usuario
    user_input = st.text_input("Hazme una pregunta sobre automoción:")

    if user_input:
        # Procesa la pregunta del usuario y genera una respuesta
        response = generate_response(user_input)
        st.text_area("Respuesta:", value=response, height=200)

def generate_response(user_input):
    # Define el prompt para la consulta al modelo GPT
    prompt = f"Me gustaría saber más sobre {user_input}. Soy un experto en ventas, mecánica y automoción."

    # Realiza la consulta al modelo GPT-3.5
    try:
        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=150
        )
        response = completion.choices[0].text.strip()
    except Exception as e:
        response = "Lo siento, no pude encontrar una respuesta en este momento."

    return response

# Ejecuta la interfaz de usuario del chatbot
if __name__ == "__main__":
    chat_ui()
