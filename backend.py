from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "your_api_here"  

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_prompt = request.json.get("prompt")
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "meta-llama/llama-3.3-8b-instruct:free",
        "messages": [{"role": "user", "content": user_prompt}]
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
