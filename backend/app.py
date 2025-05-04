from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from openai_utils import ask_assistant
import os

app = Flask(__name__)
CORS(app)

with open("allowed_domains.json") as f:
    allowed_domains = json.load(f)["allowed_domains"]

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    origin = request.headers.get("Origin", "")
    domain = origin.replace("http://", "").replace("https://", "").split(":")[0]

    if domain not in allowed_domains:
        return jsonify({"error": "Dominio no autorizado"}), 403

    message = data.get("message", "")
    assistant_id = data.get("assistant_id", "")

    if not assistant_id:
        return jsonify({"error": "assistant_id es requerido"}), 400

    reply = ask_assistant(message, assistant_id)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
