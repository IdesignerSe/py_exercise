# Duelo entre Modelos AI (Flask + Ollama)

Este proyecto muestra cómo crear un sistema donde dos modelos de IA interactúan:

Modelo A (Llama 3.1) responde a una pregunta.

Modelo B (Qwen 0.6B) evalúa críticamente la respuesta.

El usuario inspecciona los resultados desde un front‑end web.

Incluye backend en Flask, front‑end HTML y ejecución local con Ollama.

🚀 Requisitos previos
Antes de ejecutar el proyecto, asegúrate de tener instalado:

✔ Python 3.10
Recomendado usar Conda para manejar entornos.

✔ Ollama
Descargar desde:
https://ollama.com/download

✔ Modelos necesarios en Ollama

Ejecuta en terminal:

ollama pull llama3.1:8b
ollama pull qwen3:0.6b

Verifica que están instalados:

ollama list

Debe mostrar:

llama3.1:8b
qwen3:0.6b

✔ Flask
Instálalo dentro del entorno del proyecto:

pip install flask

📁 Estructura del proyecto
Tu carpeta debe verse así:

py_exercise/
│
├── app.py
├── duelo_modelos.py        ← versión consola (opcional)
│
└── templates/
      ├── index.html        ← tu archivo original
      └── duelo.html        ← front-end del duelo entre modelos

⚙️ Configuración del entorno
Crear entorno (si aún no existe):

conda create -n py310_ollama python=3.10

Activarlo:

conda activate py310_ollama

Instalar Flask:

pip install flask

Verificar Ollama:

ollama list

¿Qué hace este proyecto?
Este sistema permite:

1. Escribir una pregunta desde el navegador
Ejemplo: 
" Explica brevemente Fibonacci. "

2. Modelo A (Llama 3.1) responde
Ejemplo:
" La serie de Fibonacci comienza con 0 y 1, y cada número es la suma de los dos anteriores. "

3. Modelo B (Qwen 0.6B) evalúa la respuesta
Ejemplo:

Correcto

Falta mencionar ejemplos

Cómo mejorar

Errores conceptuales

4. El usuario inspecciona la respuesta desde el front‑end
Interfaz limpia y funcional.

🌐 Ejecutar el servidor Flask
Desde la carpeta del proyecto:

python app.py

Si todo está correcto, verás:
Running on http://127.0.0.1:5000

🖥️ Usar el front‑end
Abre en tu navegador:
http://127.0.0.1:5000/duelo


Ahí podrás:

Escribir preguntas

Ver respuestas del Modelo A

Ver evaluaciones del Modelo B

🧩 Archivos principales
app.py
Contiene:

Rutas Flask

Lógica del duelo entre modelos

Endpoint /api/duelo

Render de duelo.html

templates/duelo.html
Interfaz web para interactuar con los modelos.

🧪 Versión consola (opcional)
Puedes ejecutar:
python duelo_modelos.py

Esta versión incluye:

Ciclo iterativo

Aprobación humana

Rechazo y nueva respuesta

🛠️ Mejoras futuras
Botones “Aceptar / Rechazar” en el front‑end

Historial de respuestas

Selector de modelos

Streaming de tokens

Diseño con Tailwind o Bootstrap

📄 Licencia
Uso educativo y experimental.
