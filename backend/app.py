from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from openai_utils import ask_assistant
import os

app = Flask(__name__)

# Cargar dominios permitidos
try:
    with open("allowed_domains.json") as f:
        allowed_origins = json.load(f).get("allowed_domains", [])
    
    # Convertir a formato de orígenes completos para CORS
    allowed_origins = [f"http://{domain}" for domain in allowed_origins] + \
                     [f"https://{domain}" for domain in allowed_origins]
    
    # Agregar versiones con puerto para desarrollo local
    local_origins = []
    for origin in allowed_origins:
        if "localhost" in origin or "127.0.0.1" in origin:
            for port in ["3000", "5000", "5500", "8000", "8080"]:
                local_origins.append(f"{origin}:{port}")
    
    allowed_origins.extend(local_origins)
    
    # Configurar CORS con los orígenes permitidos
    cors_config = {
        "origins": allowed_origins,
        "methods": ["GET", "POST"],
        "allow_headers": ["Content-Type"]
    }
    CORS(app, resources={r"/*": cors_config})
    
except Exception as e:
    print(f"Error configurando CORS: {str(e)}")
    # En caso de error, permitir todo en modo desarrollo
    CORS(app)

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    """Endpoint simple para verificar que el servidor está funcionando"""
    return jsonify({"status": "ok", "message": "El servidor está en línea"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    
    # Validación de mensaje y assistant_id
    message = data.get("message", "")
    assistant_id = data.get("assistant_id", "")

    if not assistant_id:
        return jsonify({"error": "assistant_id es requerido"}), 400

    reply = ask_assistant(message, assistant_id)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)