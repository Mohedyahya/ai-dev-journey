# Day 13 - Smart Agent Project: Prompt Engineering v2.0
from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)

# Store chat history
messages = []

# ADVANCED SYSTEM PROMPT - Prompt Engineering
SYSTEM_PROMPT = """You are Smart Agent v2.0, an expert AI assistant built by Mohedyahya.
Your personality: professional, friendly, concise, and helpful.
Rules:
1. Answer in the same language as the user (Arabic or English).
2. Keep answers under 3 sentences unless asked for details.
3. If you don't know something, say "I don't know yet" honestly.
4. Always greet new users warmly.
5. Format lists with numbers."""

# Few-shot examples embedded in prompt
FEW_SHOT_EXAMPLES = """
Example 1:
User: What is Python?
Agent: Python is a powerful programming language. It is easy to learn and used in AI, web, and data science.

Example 2:
User: مرحبا
Agent: أهلاً وسهلاً! أنا الوكيل الذكي. كيف يمكنني مساعدتك اليوم؟
"""

def build_prompt(user_question):
    """Build advanced prompt with context and examples"""
    prompt = SYSTEM_PROMPT + "\n" + FEW_SHOT_EXAMPLES + "\n"
    
    # Add conversation context (last 4 messages)
    prompt += "\n--- Conversation History ---\n"
    for msg in messages[-4:]:
        role = "User" if msg["role"] == "user" else "Agent"
        prompt += role + ": " + msg["content"] + "\n"
    
    prompt += "\nUser: " + user_question + "\nAgent:"
    return prompt

def ask_ai(question):
    """Connect to Ollama with advanced prompting"""
    full_prompt = build_prompt(question)
    
    try:
        url = "http://localhost:11434/api/generate"
        data = {
            "model": "llama3.1",
            "prompt": full_prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "num_predict": 150
            }
        }
        response = requests.post(url, json=data, timeout=60)
        result = response.json()
        return result["response"].strip()
    except Exception as e:
        # Advanced mock mode with context awareness
        return smart_mock_reply(question)

def smart_mock_reply(question):
    """Smart fallback with better logic"""
    q = question.lower()
    
    # Greeting detection
    if any(word in q for word in ["hello", "hi", "مرحبا", "اهلا", "سلام"]):
        return "Hello! I am Smart Agent v2.0 with Prompt Engineering. How can I assist you today?"
    
    # Python questions
    if "python" in q:
        return "Python is a versatile programming language. It powers AI, web development, and automation. What would you like to build?"
    
    # Weather questions
    if "weather" in q:
        return "I can check weather using APIs! In a real setup, I would fetch live data for your city."
    
    # Name questions
    if "name" in q:
        return "My name is Smart Agent v2.0. I was built by Mohedyahya as part of the Smart Agent Project."
    
    # Price/cost
    if any(word in q for word in ["price", "cost", "سعر", "ثمن"]):
        return "I can help you calculate prices or build a pricing bot. What product are you asking about?"
    
    # Help
    if "help" in q or "مساعدة" in q:
        return "I can help with: Python coding, answering questions, checking weather, and customer management. What do you need?"
    
    # Default with context hint
    return "That's an interesting question about '" + question + "'. I'm learning more every day. Could you tell me more details?"

@app.route("/")
def home():
    return render_template("chat_v2.html", messages=messages)

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.form["message"]
    
    # Add user message
    messages.append({"role": "user", "content": user_msg})
    
    # Get AI response with advanced prompting
    bot_reply = ask_ai(user_msg)
    
    # Add bot message
    messages.append({"role": "bot", "content": bot_reply})
    
    # Keep only last 20 messages to save memory
    if len(messages) > 20:
        messages.pop(0)
        messages.pop(0)
    
    return redirect("/")

@app.route("/clear")
def clear():
    messages.clear()
    return redirect("/")

@app.route("/api/info")
def info():
    return json.dumps({
        "agent": "Smart Agent v2.0",
        "feature": "Prompt Engineering",
        "mode": "ollama" if False else "mock",
        "history_count": len(messages),
        "temperature": 0.7
    })

if __name__ == "__main__":
    print("=" * 50)
    print("SMART AGENT v2.0 - Prompt Engineering")
    print("Open: http://localhost:5000")
    print("=" * 50)
    app.run(host="0.0.0.0", port=5000, debug=True)

