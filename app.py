import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get("name", "Recruto")
    message = request.args.get("message", "Давай дружить")
    return f"Hello {name}! {message}!"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Используем порт из переменной окружения
    app.run(host="0.0.0.0", port=port)
