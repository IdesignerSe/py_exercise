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
    print("=== Paso 4: Aprobación humana ===\n")

    pregunta = "Explica brevemente qué es la teoría de conjuntos."
    respuesta_a = modelo_a_responde(pregunta)
    evaluacion_b = modelo_b_evalua(respuesta_a)

    print("Pregunta:", pregunta, "\n")
    print("Respuesta del Modelo A:\n", respuesta_a, "\n")
    print("Evaluación del Modelo B:\n", evaluacion_b, "\n")

    decision = input("¿Aceptar la respuesta del Modelo A? (si/no): ").strip().lower()

    if decision == "si":
        print("\n✔ Respuesta aceptada por el humano responsable.")
    else:
        print("\n✘ Respuesta rechazada por el humano responsable.")
        print("Puedes pedir una nueva respuesta o terminar el proceso.")

if __name__ == "__main__":
    main()