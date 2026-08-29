# Day 9 - Smart Agent Project: Weather Agent
import json
import requests

print("=" * 50)
print("SMART AGENT: Weather Checker")
print("=" * 50)

def get_weather(city):
    """Fetch weather from API or return mock data"""
    try:
        # Free weather API (no key needed)
        url = "https://wttr.in/" + city + "?format=j1"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        temp = data["current_condition"][0]["temp_C"]
        desc = data["current_condition"][0]["weatherDesc"][0]["value"]
        humidity = data["current_condition"][0]["humidity"]
        
        return {
            "city": city,
            "temp": temp,
            "desc": desc,
            "humidity": humidity,
            "source": "live API"
        }
    except:
        # Offline fallback (mock data)
        mock_db = {
            "sanaa": {"temp": 22, "desc": "Clear", "humidity": 45},
            "aden": {"temp": 32, "desc": "Sunny", "humidity": 70},
            "dubai": {"temp": 38, "desc": "Hot", "humidity": 60},
            "london": {"temp": 15, "desc": "Rainy", "humidity": 80}
        }
        
        city_key = city.lower()
        if city_key in mock_db:
            return {
                "city": city,
                "temp": mock_db[city_key]["temp"],
                "desc": mock_db[city_key]["desc"],
                "humidity": mock_db[city_key]["humidity"],
                "source": "offline mock"
            }
        else:
            return None

# Main program
while True:
    print("\n1. Check weather")
    print("2. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        city = input("Enter city name: ")
        result = get_weather(city)
        
        if result:
            print("\n--- WEATHER REPORT ---")
            print("City: " + result["city"])
            print("Temperature: " + result["temp"] + " C")
            print("Condition: " + result["desc"])
            print("Humidity: " + result["humidity"] + "%")
            print("Source: " + result["source"])
            print("----------------------")
        else:
            print("City not found in offline database")
    
    elif choice == "2":
        print("Goodbye!")
        break

print("=" * 50)

