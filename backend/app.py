from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from openai_utils import ask_assistant

app = Flask(__name__)

# Cargar dominios permitidos
try:
    with open("allowed_domains.json") as f:
        allowed_domains = json.load(f).get("allowed_domains", [])
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error al cargar allowed_domains.json: {e}")
    allowed_domains = ["localhost", "127.0.0.1"]

# Configurar CORS más específico
CORS(app, origins=["http://" + domain for domain in allowed_domains] + 
               ["https://" + domain for domain in allowed_domains])

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Validar el formato JSON
        if not request.is_json:
            return jsonify({"error": "Se requiere formato JSON"}), 400
            
        data = request.get_json()
        
        # Validar campos requeridos
        message = data.get("message")
        assistant_id = data.get("assistant_id")
        
        if not message:
            return jsonify({"error": "El campo 'message' es requerido"}), 400
        if not assistant_id:
            return jsonify({"error": "El campo 'assistant_id' es requerido"}), 400

        # Enviar mensaje al asistente
        reply = ask_assistant(message, assistant_id)
        
        # Verificar si hay un error
        if reply.startswith("[ERROR]"):
            return jsonify({"error": reply}), 500
            
        return jsonify({"response": reply})
        
    except Exception as e:
        return jsonify({"error": f"Error del servidor: {str(e)}"}), 500

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    """Endpoint para verificar que el servidor está funcionando"""
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    # Mejor configuración para producción
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=debug_mode, host="0.0.0.0", port=port)