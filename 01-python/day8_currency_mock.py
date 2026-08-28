# Day 8 - Currency Agent (Mock Mode)
print("=" * 50)
print("SMART AGENT: Currency Checker (Offline Mode)")
print("=" * 50)

# Mock rates (simulating API response)
rates = {
    "USD": {"YER": 250.0, "SAR": 3.75, "EGP": 30.9},
    "SAR": {"YER": 66.7, "USD": 0.27, "EGP": 8.24},
    "YER": {"USD": 0.004, "SAR": 0.015, "EGP": 0.12}
}

while True:
    print("\n1. Check rate")
    print("2. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        base = input("From (USD/SAR/YER): ").upper()
        target = input("To (USD/SAR/YER): ").upper()
        
        if base in rates and target in rates[base]:
            rate = rates[base][target]
            print("1 " + base + " = " + str(rate) + " " + target)
            
            amount = input("Amount: ")
            result = float(amount) * rate
            print(amount + " " + base + " = " + str(result) + " " + target)
        else:
            print("Rate not available in mock data")
    
    elif choice == "2":
        print("Goodbye!")
        break

print("=" * 50)

