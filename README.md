# Aplicación de Chatbot con OpenAI Assistant API

Esta aplicación implementa un chatbot interactivo utilizando la API de OpenAI Assistant. Proporciona una interfaz de usuario amigable que se puede integrar fácilmente en cualquier sitio web.

## 📋 Características

- **Chat flotante** que se puede integrar en cualquier página web
- **Interfaz de usuario moderna y responsiva**
- **Indicador de escritura** durante la espera de respuestas
- **Manejo de errores** para problemas de conexión y CORS
- **Configuración flexible** para personalizar el comportamiento del chatbot

## 🗂️ Estructura del Proyecto

```
.
├── backend/
│   ├── app.py                 # Servidor Flask con endpoints REST
│   ├── openai_utils.py        # Utilidades para interactuar con la API de OpenAI
│   └── allowed_domains.json   # Configuración de dominios permitidos para CORS
├── frontend/
│   ├── index.html             # Página HTML con el widget de chat integrado
│   └── chatbot.js             # Lógica de JavaScript para interactuar con el backend
└── .env                       # Variables de entorno (crear desde .env.example)
```

## 🔧 Requisitos

- Python 3.7+
- Cuenta de OpenAI con acceso a la API de Assistants
- Un Assistant configurado en la plataforma OpenAI con su ID correspondiente

## 🚀 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/your-username/chatbot-app.git
   cd chatbot-app
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python3 -m venv chatbot-env
   
   # En Linux/macOS:
   source chatbot-env/bin/activate
   
   # En Windows:
   chatbot-env\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   python3 -m pip install flask flask-cors openai python-dotenv
   ```

4. Configura las variables de entorno:
   ```bash
   cp .env.example .env
   # Edita el archivo .env con tu API key de OpenAI
   ```

## 💻 Uso

1. Inicia el servidor backend:
   ```bash
   cd backend
   python3 app.py
   ```

2. Para probar la aplicación:
   - Abre `frontend/index.html` en tu navegador, o
   - Sirve los archivos a través de un servidor web estático

3. El widget de chat aparecerá en la esquina inferior derecha de la página. Haz clic en el botón para abrir el chat y comenzar a interactuar con el asistente.

## ⚙️ Configuración

### Backend

El backend tiene las siguientes configuraciones principales:

- **CORS**: Modifica `allowed_domains.json` para añadir los dominios desde los cuales se permitirá el acceso al API.
- **Variables de entorno**: Configura tu `OPENAI_API_KEY` en el archivo `.env`.

### Frontend

En el archivo `index.html`, puedes modificar:

- `BACKEND_URL`: La URL del servidor backend (por defecto: "http://localhost:5000").
- `ASSISTANT_ID`: El ID de tu asistente de OpenAI (por defecto: "asst_i2ivyEjwxcYQT2QFwuioPzKh").
- `AVATAR_URL`: URL para el avatar del asistente (utiliza DiceBear por defecto).

## 🎨 Personalización

### Estilo del Chat

Puedes personalizar el aspecto visual del chat modificando las reglas CSS en `frontend/index.html`. Los elementos principales incluyen:

- `.chat-widget`: Contenedor principal del widget
- `.chat-button`: Botón flotante para abrir el chat
- `.chat-container`: Contenedor del área de chat
- `.message`: Estilo general de los mensajes
- `.user-message`, `.assistant-message`, `.system-message`: Estilos específicos por tipo de mensaje

### Funcionalidad

Para modificar el comportamiento del chatbot:

- Ajusta la lógica de manejo de mensajes en `frontend/chatbot.js`
- Modifica la interacción con la API de OpenAI en `backend/openai_utils.py`
- Añade nuevos endpoints o funcionalidades en `backend/app.py`

## 🔍 Diagnóstico de Problemas

### Problemas Comunes

- **Error de API Key**: Asegúrate de que la variable de entorno `OPENAI_API_KEY` esté correctamente configurada en tu sistema o en el archivo `.env`.

- **Error de CORS**: Si recibes errores de CORS, verifica:
  1. Que el dominio desde el que accedes esté en la lista de `allowed_domains.json`
  2. Que el servidor backend esté ejecutándose
  3. Que los encabezados CORS estén configurados correctamente

- **Error de conexión con el backend**:
  1. Verifica que el servidor Flask esté en ejecución
  2. Comprueba que las URLs en el frontend coincidan con donde está desplegado el backend
  3. Revisa la consola del navegador para errores específicos

- **Errores con la API de OpenAI**:
  1. Verifica que tu API key tenga suficientes créditos
  2. Asegúrate de que el Assistant ID exista y esté correctamente configurado
  3. Revisa los logs del servidor para mensajes de error específicos

## 📝 Licencia

Este proyecto está disponible bajo la licencia MIT.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, siente libre de enviar pull requests o abrir issues para mejorar este proyecto.