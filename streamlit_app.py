import streamlit as st
from streamlit_toyui import chat_ui
from langchain.chains import ChatChain
from langchain.schema import UserMessage
from langchain.skills import OpenAISkill

# Configurando el skill de OpenAI con personalización de modelo
def expert_mechanics_sales_automotive_prompt(message):
    return f"""
    Soy un experto en mecánica, ventas y automoción con más de 20 años de experiencia en la industria.
    He trabajado con numerosas marcas de automóviles y tengo un profundo conocimiento de los motores,
    las últimas tecnologías en automóviles y estrategias efectivas de venta de vehículos. ¿Cómo puedo ayudarte hoy?
    Pregunta: {message}
    Respuesta:"""

openai_skill = OpenAISkill(
    api_key="sk-proj-9FWmlDJLMjweNyRz8deJT3BlbkFJde76yd3V5BxuGJKdAx6R",
    prompt_function=expert_mechanics_sales_automotive_prompt
)

# Creando la cadena de chat con el skill configurado.
chat_chain = ChatChain(skills=[openai_skill])

# Streamlit App
def main():
    st.title("Chatbot Experto en Mecánica, Ventas y Automoción")

    # Usamos la función chat_ui de ToyUI para manejar la interfaz de chat.
    chat_log = chat_ui("chat", key="chat")

    # Verificar si hay mensajes nuevos y responder
    if chat_log.new_message:
        user_message = chat_log.new_message.text
        # Creamos un UserMessage, necesario para pasar al chat chain.
        user_message_obj = UserMessage(text=user_message, sender_id="user")
        # Usamos el chat chain para obtener una respuesta.
        response = chat_chain.run(user_message_obj)
        # Agregamos la respuesta al chat
        chat_log.append_message("Bot", response.text)

if __name__ == "__main__":
    main()
