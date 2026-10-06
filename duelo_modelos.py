import ollama

def modelo_a_responde(pregunta):
    respuesta = ollama.generate(
        model="llama3.1:8b",
        prompt=pregunta
    )
    return respuesta["response"]

def modelo_b_evalua(respuesta_a):
    # Aquí luego pondremos el modelo B
    pass

def main():
    print("Sistema de duelo entre modelos — Paso 1 completado.")
    print("Aún no hay lógica, solo estructura base.")

if __name__ == "__main__":
    main()