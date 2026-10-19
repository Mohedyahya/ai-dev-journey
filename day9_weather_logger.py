# Day 9 - Save weather results to file
import json
from datetime import datetime

print("=" * 50)
print("AGENT: Weather Logger")
print("=" * 50)

def log_weather(city, temp, condition):
    """Save weather to history file"""
    entry = {
        "time": str(datetime.now()),
        "city": city,
        "temp": temp,
        "condition": condition
    }
    
    # Read existing history
    try:
        with open("weather_history.json", "r") as f:
            history = json.load(f)
    except:
        history = []
    
    # Add new entry
    history.append(entry)
    
    # Save back
    with open("weather_history.json", "w") as f:
        json.dump(history, f, indent=2)
    
    print("SAVED to weather_history.json")

# Test
log_weather("Sanaa", "22", "Clear")
log_weather("Aden", "32", "Sunny")

print("\nAGENT: Weather history saved!")
print("=" * 50)

