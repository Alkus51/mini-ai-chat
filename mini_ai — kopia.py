from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Loads the .env file

app = Flask(__name__)

# Use your secret key from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    message = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        reply = response.choices[0].message["content"].strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(port=5000)
