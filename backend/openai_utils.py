import os
from openai import OpenAI
import time

# Verificar la existencia de la API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("OPENAI_API_KEY no está configurada como variable de entorno")

# Inicializar el cliente con la API actual
client = OpenAI(api_key=api_key)

def ask_assistant(user_message, assistant_id):
    try:
        # Validar el assistant_id
        if not assistant_id or not isinstance(assistant_id, str):
            return "[ERROR] ID de asistente inválido"
            
        # Crear un nuevo thread para cada mensaje
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

        # Esperar a que termine el run (con polling y timeout)
        timeout = 30  # segundos
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                return "[ERROR] Tiempo de espera excedido"
                
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
        for msg in messages.data:
            if msg.role == "assistant":
                return msg.content[0].text.value

        return "[ERROR] No se encontró respuesta del asistente."

    except Exception as e:
        return f"[ERROR] {str(e)}"