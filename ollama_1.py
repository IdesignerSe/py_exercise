
import ollama

response = ollama.generate(
    model="qwen3:0.6b",
    prompt="Hola Heb, probando Ollama desde Python."
)

print(response["response"])