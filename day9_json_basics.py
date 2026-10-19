# Day 9 - Smart Agent Project: JSON Basics
import json

print("=" * 45)
print("AGENT: Learning JSON")
print("=" * 45)

# JSON is just text that looks like a Python dictionary
json_text = '{"city": "Sanaa", "temp": 22, "unit": "C"}'

# Convert JSON text to Python dictionary
data = json.loads(json_text)

print("\nCity: " + data["city"])
print("Temperature: " + str(data["temp"]) + data["unit"])

# Convert Python dictionary to JSON text
agent_data = {
    "name": "Smart Agent",
    "version": 1.0,
    "skills": ["chat", "weather", "files"]
}

json_output = json.dumps(agent_data, indent=2)
print("\nAgent JSON:")
print(json_output)

print("\n" + "=" * 45)

