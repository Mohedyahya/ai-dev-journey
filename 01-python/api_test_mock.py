# Day 8 - Smart Agent Project: Mock API (No Internet Needed)
import json

print("=" * 45)
print("AGENT: Simulating API Response")
print("=" * 45)

# This simulates what requests.get(url).json() returns
mock_response = {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur"
}

print("\n--- SIMULATED DATA (like requests.json()) ---")
print("User ID: " + str(mock_response["userId"]))
print("Post ID: " + str(mock_response["id"]))
print("Title: " + mock_response["title"])
print("Body: " + mock_response["body"][:50] + "...")

print("\n" + "=" * 45)
print("SUCCESS: Agent learned JSON structure!")
print("=" * 45)

