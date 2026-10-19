# Day 12 - Smart Agent Project: Flask + Ollama Chatbot
from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)

# Store chat history
messages = []

def ask_ai(question):
    """Connect to Ollama or use mock fallback"""
    try:
        url = "http://localhost:11434/api/generate"
        data = {
            "model": "llama3.1",
            "prompt": "You are Smart Agent, a helpful AI assistant. Answer briefly.\n\nUser: " + question + "\nAgent:",
            "stream": False
        }
        response = requests.post(url, json=data, timeout=30)
        result = response.json()
        return result["response"]
    except:
        # MOCK MODE for Termux / offline
        q = question.lower()
        if "hello" in q or "hi" in q:
            return "Hello! I am Smart Agent powered by AI. How can I help?"
        elif "name" in q:
            return "My name is Smart Agent. I am connected to an AI brain."
        elif "python" in q:
            return "Python is the language I was built with. It is powerful!"
        elif "weather" in q:
            return "I can check weather using my API skills from Day 9!"
        elif "time" in q:
            return "I do not have a clock yet, but I am learning fast!"
        else:
            return "That is an interesting question about '" + question + "'. Tell me more!"

@app.route("/")
def home():
    return render_template("chat.html", messages=messages)

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.form["message"]
    
    # Add user message
    messages.append({"role": "user", "content": user_msg})
    
    # Get AI response
    bot_reply = ask_ai(user_msg)
    
    # Add bot message
    messages.append({"role": "bot", "content": bot_reply})
    
    return redirect("/")

@app.route("/clear")
def clear():
    messages.clear()
    return redirect("/")

if __name__ == "__main__":
    print("=" * 50)
    print("SMART AGENT CHATBOT v1.0")
    print("Open: http://10.124.231.49:5000")
    print("=" * 50)
    app.run(host="0.0.0.0", port=5000, debug=True)

