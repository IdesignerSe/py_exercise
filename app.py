from flask import Flask, render_template, request, jsonify
import ollama
import time

app = Flask(__name__)

# ============================================================
# MODELO A: responde (Llama 3.1 8B)
# ============================================================
def modelo_a_responde(pregunta, idioma):
    prompt_final = f"""
Responde en el idioma indicado: {idioma}

Pregunta:
{pregunta}
"""

    start_a = time.time()
    respuesta_a_raw = ollama.generate(
        model="llama3.1:8b",
        prompt=prompt_final
    )
    tiempo_a = time.time() - start_a

    return {
        "texto": respuesta_a_raw["response"],
        "tiempo": tiempo_a,
        "tokens": respuesta_a_raw.get("eval_count", 0),
        "prompt_tokens": respuesta_a_raw.get("prompt_eval_count", 0)
    }

# ============================================================
# MODELO B: evalúa (Qwen 0.6B)
# ============================================================
def modelo_b_evalua(respuesta_a_texto, idioma):
    prompt_evaluacion = f"""
Evalúa la siguiente respuesta generada por otro modelo.
Responde en el idioma: {idioma}

RESPUESTA DEL MODELO A:
{respuesta_a_texto}

Quiero que me digas:
- Si la explicación es correcta.
- Si falta algo importante.
- Si hay errores conceptuales.
- Cómo mejorarla.
"""

    start_b = time.time()
    evaluacion_b_raw = ollama.generate(
        model="qwen3:0.6b",
        prompt=prompt_evaluacion
    )
    tiempo_b = time.time() - start_b

    return {
        "texto": evaluacion_b_raw["response"],
        "tiempo": tiempo_b,
        "tokens": evaluacion_b_raw.get("eval_count", 0),
        "prompt_tokens": evaluacion_b_raw.get("prompt_eval_count", 0)
    }

# -----------------------------
# RUTA DEL FRONT-END
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
    idioma = data["idioma"]  # viene del selector del frontend

    modelo_a = modelo_a_responde(pregunta, idioma)
    modelo_b = modelo_b_evalua(modelo_a["texto"], idioma)

    return jsonify({
        "idioma": idioma,
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