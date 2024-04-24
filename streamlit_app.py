import streamlit as st

def obtener_respuesta(mensaje):
    mensaje = mensaje.lower().strip()
    if "motor" in mensaje:
        return "Los problemas de motor pueden ser variados, ¿podrías especificar si es un ruido, un fallo en el arranque o algún otro síntoma?"
    elif "precio" in mensaje:
        return "El precio de los vehículos varía según el modelo, el año y el estado del vehículo. ¿Estás interesado en algún modelo en particular?"
    elif "llantas" in mensaje:
        return "Las llantas adecuadas dependen del tipo de vehículo y el uso que le das. Por ejemplo, para conducción todo terreno, las llantas deben tener un mejor agarre."
    elif "descuento" in mensaje:
        return "Actualmente tenemos promociones en varios modelos. ¿Te interesa algún modelo en específico para darte más detalles sobre los descuentos disponibles?"
    else:
        return "Lo siento, no entendí bien tu pregunta. ¿Puedes dar más detalles o hacer otra pregunta?"

# HTML básico para una interfaz de chat
chat_html = """
<div style='border: 1px solid #ccc; padding: 10px; height: 300px; overflow-y: scroll; margin-bottom: 20px;'>
    <!-- Aquí irán los mensajes del chat -->
    %s
</div>
<input type='text' id='message_input' placeholder='Escribe un mensaje...' style='width: 78%; margin-right: 10px;'>
<button onclick='sendMessage()'>Enviar</button>
<script>
function sendMessage() {
    const input = document.getElementById('message_input');
    const message = input.value;
    input.value = '';
    if (message) {
        window.parent.postMessage({type: 'streamlit:setComponentValue', args: {data: message}}, '*');
    }
}
</script>
"""

# Inicializa el estado si no existe
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Agregar un nuevo mensaje si se recibe uno
if st.session_state.widget_values and 'default' in st.session_state.widget_values:
    user_message = st.session_state.widget_values['default']
    st.session_state.messages.append(f"Tú: {user_message}")
    # Obtener la respuesta del "experto"
    bot_response = obtener_respuesta(user_message)
    st.session_state.messages.append(f"Experto: {bot_response}")

# Formatear y mostrar los mensajes en el HTML
formatted_messages = "<br>".join(st.session_state.messages)
st.components.v1.html(chat_html % formatted_messages, height=400)
