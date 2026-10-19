# Day 8 - Smart Agent Project: Connect to the Internet
import requests

print("=" * 45)
print("AGENT: Testing Internet Connection")
print("=" * 45)

# Test 1: Simple GET request
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print("\nURL: " + url)
print("Status Code: " + str(response.status_code))

if response.status_code == 200:
    print("SUCCESS: Connection established!")
    
    # Convert JSON to Python dictionary
    data = response.json()
    
    print("\n--- DATA RECEIVED ---")
    print("User ID: " + str(data["userId"]))
    print("Post ID: " + str(data["id"]))
    print("Title: " + data["title"])
    print("Body: " + data["body"][:50] + "...")
else:
    print("FAILED: Could not connect")

print("\n" + "=" * 45)

