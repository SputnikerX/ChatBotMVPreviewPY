// Configuración del chatbot
const BACKEND_URL = "http://localhost:5000";
const ASSISTANT_ID = "asst_i2ivyEjwxcYQT2QFwuioPzKh";

// Elementos del DOM
let userInput;
let chatResponse;
let sendButton;

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
  userInput = document.getElementById("userInput");
  chatResponse = document.getElementById("chatResponse");
  sendButton = document.getElementById("sendButton");
  
  // Evento para enviar al presionar Enter
  userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      sendMessage();
    }
  });
  
  // Verificar la conexión con el backend
  checkBackendConnection();
});

/**
 * Verifica la conexión con el backend
 */
async function checkBackendConnection() {
  try {
    const res = await fetch(`${BACKEND_URL}/healthcheck`);
    if (res.ok) {
      console.log("Conexión con el backend establecida");
    } else {
      showError("El servidor está en línea pero reporta un error");
    }
  } catch (err) {
    showError("No se puede conectar con el backend. Asegúrate de que el servidor esté en ejecución.");
  }
}

/**
 * Envía el mensaje al backend y muestra la respuesta
 */
async function sendMessage() {
  // Validación básica
  const message = userInput.value.trim();
  if (!message) return;
  
  // UI feedback
  const originalText = chatResponse.innerText;
  chatResponse.innerText = "Procesando...";
  userInput.disabled = true;
  sendButton.disabled = true;
  
  try {
    const res = await fetch(`${BACKEND_URL}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ 
        message: message, 
        assistant_id: ASSISTANT_ID 
      })
    });
    
    const data = await res.json();
    
    if (res.ok && data.response) {
      displayResponse(data.response);
      userInput.value = ""; // Limpiar input después de enviar
    } else {
      showError(data.error || "Error desconocido en la respuesta");
    }
  } catch (err) {
    showError(`Error de conexión: ${err.message}`);
  } finally {
    userInput.disabled = false;
    sendButton.disabled = false;
    userInput.focus();
  }
}

/**
 * Muestra la respuesta del chatbot
 */
function displayResponse(text) {
  chatResponse.innerText = text;
}

/**
 * Muestra un mensaje de error
 */
function showError(message) {
  chatResponse.innerHTML = `<span class="error">${message}</span>`;
  console.error(message);
}
