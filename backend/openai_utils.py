import openai
import time
import os

# Asegúrate de tener esta variable de entorno exportada en tu sistema:
# export OPENAI_API_KEY=sk-...
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai

def ask_assistant(user_message, assistant_id):
    try:
        # ✅ Crear un nuevo thread para cada mensaje
        thread = client.beta.threads.create()

        # Agregar el mensaje del usuario
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_message
        )

        # Iniciar el run con el Assistant ID personalizado
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id
        )

        # Esperar a que termine el run (con polling)
        while True:
            run_status = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            if run_status.status == "completed":
                break
            elif run_status.status in ("failed", "cancelled", "expired"):
                return f"[ERROR] El run falló con estado: {run_status.status}"
            time.sleep(1)  # Espera 1 segundo antes de volver a verificar

        # Obtener el último mensaje del asistente
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        for msg in reversed(messages.data):
            if msg.role == "assistant":
                return msg.content[0].text.value

        return "[ERROR] No se encontró respuesta del asistente."

    except Exception as e:
        return f"[ERROR] {str(e)}"
