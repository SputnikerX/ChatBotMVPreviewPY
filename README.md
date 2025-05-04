# Aplicación de Chatbot con OpenAI Assistant API

Esta aplicación es un chatbot simple que utiliza la API de OpenAI Assistant para procesar mensajes.

## Estructura del Proyecto

```
.
├── backend/
│   ├── app.py                 # Servidor Flask
│   ├── openai_utils.py        # Utilidades para la API de OpenAI
│   └── allowed_domains.json   # Dominios permitidos para CORS
├── frontend/
│   ├── index.html             # Página HTML principal
│   └── chatbot.js             # Script de JavaScript para la UI
└── .env                       # Variables de entorno (crear desde .env.example)
```

## Requisitos

- Python 3.7+
- Cuenta de OpenAI con acceso a la API de Assistants
- Un asistente creado en la plataforma OpenAI

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/chatbot-app.git
   cd chatbot-app
   ```

2. Crea un entorno virtual y actívalo:
   ```
   python -m venv chatbot-env
   source chatbot-env/bin/activate  # En Windows: chatbot-env\Scripts\activate
   ```

3. Instala las dependencias:
   ```
   pip install flask flask-cors openai python-dotenv
   ```

4. Configura las variables de entorno:
   ```
   cp .env.example .env
   # Edita el archivo .env con tu API key de OpenAI
   ```

## Uso

1. Inicia el servidor backend:
   ```
   cd backend
   python app.py
   ```

2. Abre el archivo `frontend/index.html` en tu navegador o usa un servidor web estático.

3. Escribe un mensaje y presiona "Enviar" para interactuar con el chatbot.

## Personalización

- Modifica `frontend/chatbot.js` para cambiar el ID del asistente de OpenAI.
- Edita `backend/allowed_domains.json` para añadir dominios permitidos para CORS.
- Personaliza los estilos en `frontend/index.html`.

## Problemas comunes

- **Error de API Key**: Asegúrate de que la variable de entorno `OPENAI_API_KEY` esté correctamente configurada.
- **Error de CORS**: Verifica que el dominio desde el que accedes esté en la lista de dominios permitidos.
- **Error de conexión**: Asegúrate de que el servidor backend esté en ejecución.

## Licencia

Este proyecto está disponible bajo la licencia MIT.
