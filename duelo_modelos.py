import ollama

def modelo_a_responde(pregunta):
    respuesta = ollama.generate(
        model="llama3.1:8b",
        prompt=pregunta
    )
    return respuesta["response"]

def modelo_b_evalua(respuesta_a):
    prompt_evaluacion = f"""
Evalúa la siguiente respuesta generada por otro modelo:

RESPUESTA DEL MODELO A:
{respuesta_a}

Quiero que me digas:
- Si la explicación es correcta.
- Si falta algo importante.
- Si hay errores conceptuales.
- Cómo mejorarla.

Sé crítico pero justo.
"""

    evaluacion = ollama.generate(
        model="qwen3:0.6b",
        prompt=prompt_evaluacion
    )

    return evaluacion["response"]

def main():
    print("=== Paso 2: Modelo A responde ===\n")

    pregunta = "Explica brevemente qué es la teoría de conjuntos."
    respuesta_a = modelo_a_responde(pregunta)

    print("Pregunta:", pregunta, "\n")
    print("Respuesta del Modelo A:\n", respuesta_a)

if __name__ == "__main__":
    main()