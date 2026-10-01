# Qwen3:0.6B
import ollama

def chatbot():
    print("\n=== Chatbot con qwen3:0.6b ===")
    while True:
        user = input("Tú: ")
        if user.lower() in ["exit", "salir", "quit"]:
            print("Chatbot terminado.\n")
            break

        response = ollama.generate(
            model="qwen3:0.6b",
            prompt=user
        )
        print("Qwen:", response["response"])


def analizador_texto():
    print("\n=== Analizador de texto ===")
    texto = input("Ingresa el texto a analizar:\n> ")

    prompt = f"""
Analiza el siguiente texto y dame:
- Un resumen
- Palabras clave
- Sentimiento general
- Una explicación breve

Texto:
{texto}
"""

    response = ollama.generate(
        model="qwen3:0.6b",
        prompt=prompt
    )

    print("\nResultado del análisis:\n")
    print(response["response"])
    print("\n")


def generador_codigo():
    print("\n=== Generador de código ===")
    instruccion = input("Describe el código que quieres generar:\n> ")

    prompt = f"""
Genera código según esta instrucción:
{instruccion}

Incluye:
- Explicación breve
- Código funcional
"""

    response = ollama.generate(
        model="qwen3:0.6b",
        prompt=prompt
    )

    print("\nCódigo generado:\n")
    print(response["response"])
    print("\n")


def menu():
    while True:
        print("=== Menú de opciones ===")
        print("1. Chatbot")
        print("2. Analizador de texto")
        print("3. Generador de código")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            chatbot()
        elif opcion == "2":
            analizador_texto()
        elif opcion == "3":
            generador_codigo()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.\n")


if __name__ == "__main__":
    menu()