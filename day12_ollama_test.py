# Day 12 - Test Ollama Connection
import requests
import json

print("=" * 50)
print("AGENT: Testing Ollama Connection")
print("=" * 50)

def ask_ollama(question):
    try:
        url = "http://localhost:11434/api/generate"
        data = {
            "model": "llama3.1",
            "prompt": question,
            "stream": False
        }
        response = requests.post(url, json=data, timeout=30)
        result = response.json()
        return result["response"]
    except Exception as e:
        print("OLLAMA NOT FOUND: " + str(e))
        print("Using mock mode instead...")
        return "MOCK: I received your question: '" + question + "'"

# Test
question = "What is Python?"
answer = ask_ollama(question)

print("\nQUESTION: " + question)
print("ANSWER: " + answer)
print("=" * 50)

