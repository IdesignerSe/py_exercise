from flask import Flask, render_template, request, jsonify
import ollama
import time

app = Flask(__name__)

# -----------------------------
# MODELO ORIGINAL (Qwen 0.6B)
# -----------------------------
def ask_model(prompt):
    response = ollama.generate(
        model="qwen3:0.6b",
        prompt=prompt
    )
    return response["response"]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    user_text = ""

    if request.method == "POST":
        user_text = request.form["user_text"]
        mode = request.form["mode"]

        if mode == "chat":
            result = ask_model(user_text)

        elif mode == "analyze":
            prompt = f"""
Analiza este texto:
{user_text}

Dame:
- resumen
- palabras clave
- sentimiento
- explicación breve
"""
            result = ask_model(prompt)

        elif mode == "code":
            prompt = f"""
Genera código según esta instrucción:
{user_text}

Incluye explicación y código funcional.
"""
            result = ask_model(prompt)

    return render_template("index.html", result=result, user_text=user_text)


# ============================================================
# NUEVO SISTEMA: DUELO ENTRE MODELOS (Llama 3.1 vs Qwen 0.6B)
# ============================================================

# Modelo A: responde (Llama 3.1 8B)
def modelo_a_responde(pregunta):
    start_a = time.time()
    respuesta_a_raw = ollama.generate(
        model="llama3.1:8b",
        prompt=pregunta
    )
    tiempo_a = time.time() - start_a

    respuesta_a = respuesta_a_raw["response"]
    tokens_a = respuesta_a_raw.get("eval_count", 0)
    prompt_tokens_a = respuesta_a_raw.get("prompt_eval_count", 0)

    return {
        "texto": respuesta_a,
        "tiempo": tiempo_a,
        "tokens": tokens_a,
        "prompt_tokens": prompt_tokens_a
    }

# Modelo B: evalúa (Qwen 0.6B)
def modelo_b_evalua(respuesta_a_texto):
    prompt_evaluacion = f"""
Evalúa la siguiente respuesta generada por otro modelo:

RESPUESTA DEL MODELO A:
{respuesta_a_texto}

Quiero que me digas:
- Si la explicación es correcta.
- Si falta algo importante.
- Si hay errores conceptuales.
- Cómo mejorarla.

Sé crítico pero justo.
"""

    start_b = time.time()
    evaluacion_b_raw = ollama.generate(
        model="qwen3:0.6b",
        prompt=prompt_evaluacion
    )
    tiempo_b = time.time() - start_b

    evaluacion_b = evaluacion_b_raw["response"]
    tokens_b = evaluacion_b_raw.get("eval_count", 0)
    prompt_tokens_b = evaluacion_b_raw.get("prompt_eval_count", 0)

    return {
        "texto": evaluacion_b,
        "tiempo": tiempo_b,
        "tokens": tokens_b,
        "prompt_tokens": prompt_tokens_b
    }


# -----------------------------
# NUEVA RUTA PARA EL FRONT-END
# -----------------------------
@app.route("/duelo")
def duelo():
    return render_template("duelo.html")


# -----------------------------
# API PARA EL FRONT-END
# -----------------------------
@app.route("/api/duelo", methods=["POST"])
def api_duelo():
    data = request.json
    pregunta = data["pregunta"]

    modelo_a = modelo_a_responde(pregunta)
    modelo_b = modelo_b_evalua(modelo_a["texto"])

    return jsonify({
        "respuesta_a": modelo_a["texto"],
        "evaluacion_b": modelo_b["texto"],
        "tiempo_a": modelo_a["tiempo"],
        "tiempo_b": modelo_b["tiempo"],
        "tokens_a": modelo_a["tokens"],
        "tokens_b": modelo_b["tokens"],
        "prompt_tokens_a": modelo_a["prompt_tokens"],
        "prompt_tokens_b": modelo_b["prompt_tokens"]
    })


# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)