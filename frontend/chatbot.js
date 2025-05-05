/**
 * Envía el mensaje al backend y muestra la respuesta
 */
async function sendMessage() {
  // Validación básica
  const message = userInput.value.trim();
  if (!message) return;
  
  // Añade el mensaje del usuario al chat
  addMessage("Tú", message, "user");
  
  // UI feedback
  userInput.value = "";
  userInput.disabled = true;
  sendButton.disabled = true;
  showTypingIndicator();
  
  try {
    const res = await fetch(`${BACKEND_URL}/chat`, {
      method: "POST",
      headers: { 
        "Content-Type": "application/json",
        // Aseguramos que se envíe Origin en la solicitud
        "X-Requested-With": "XMLHttpRequest"
      },
      // Importante: incluir credentials para solicitudes CORS con cookies
      credentials: "include",
      body: JSON.stringify({ 
        message: message, 
        assistant_id: ASSISTANT_ID 
      })
    });
    
    hideTypingIndicator();
    
    // Comprobar si la respuesta es exitosa
    if (!res.ok) {
      // Si tenemos un error 403, probablemente es un problema de CORS/dominio
      if (res.status === 403) {
        addMessage("Sistema", "Error de acceso: Este origen no está autorizado para acceder al API. Verifica la configuración CORS.", "system");
        return;
      }
      
      // Para otros errores HTTP, intentamos obtener el mensaje
      try {
        const errorData = await res.json();
        addMessage("Sistema", errorData.error || `Error ${res.status}: ${res.statusText}`, "system");
      } catch (parseError) {
        addMessage("Sistema", `Error ${res.status}: ${res.statusText}`, "system");
      }
      return;
    }
    
    // Si llegamos aquí, la respuesta es exitosa
    const data = await res.json();
    if (data.response) {
      addMessage("Asistente", data.response, "assistant");
    } else {
      addMessage("Sistema", "El servidor respondió correctamente pero no se recibió una respuesta del asistente.", "system");
    }
    
  } catch (err) {
    hideTypingIndicator();
    
    // Detectar si es un error específico de CORS
    if (err instanceof TypeError && err.message.includes('Failed to fetch')) {
      addMessage("Sistema", "Error de conexión: No se pudo contactar con el servidor. Posible problema CORS o servidor inactivo.", "system");
    } else {
      addMessage("Sistema", `Error: ${err.message}`, "system");
    }
  } finally {
    userInput.disabled = false;
    sendButton.disabled = false;
    userInput.focus();
  }
}