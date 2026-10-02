
import ollama

response = ollama.generate(
    model="llama3.1:8b",
    prompt="Hola Heb, probando Ollama desde Python."
)

print(response["response"])