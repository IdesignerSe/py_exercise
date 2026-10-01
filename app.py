from flask import Flask, render_template, request
import ollama

app = Flask(__name__)

def ask_model(prompt):
    response = ollama.generate(
        model="qwen3:0.6b",
        prompt=prompt
    )
    return response["response"]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
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

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)