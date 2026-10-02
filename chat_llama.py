# chat_llama.py
import ollama

print("Mini‑chat con Llama 3.1 8B. Escribe 'salir' para terminar.\n")

while True:
    user_input = input("Tú: ")

    if user_input.lower() == "salir":
        print("Chat terminado.")
        break

    response = ollama.generate(
        model="llama3.1:8b",
        prompt=user_input
    )

    print("Llama 3.1:", response["response"], "\n")