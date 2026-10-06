import ollama

def modelo_a_responde(pregunta):
    respuesta = ollama.generate(
        model="llama3.1:8b",
        prompt=pregunta
    )
    return respuesta["response"]

def modelo_b_evalua(respuesta_a):
    # Se implementará en el siguiente paso
    pass

def main():
    print("=== Paso 2: Modelo A responde ===\n")

    pregunta = "Explica brevemente qué es la teoría de conjuntos."
    respuesta_a = modelo_a_responde(pregunta)

    print("Pregunta:", pregunta, "\n")
    print("Respuesta del Modelo A:\n", respuesta_a)

if __name__ == "__main__":
    main()