# Week 1 Project - Smart Agent
# Combines: Variables, Conditions, Loops, Lists, Dictionaries, Functions, Files

def load_customers():
    """Load customers from file"""
    try:
        with open("customers_db.txt", "r") as f:
            customers = []
            for line in f:
                parts = line.strip().split(" - ")
                if len(parts) == 3:
                    customers.append({
                        "name": parts[0],
                        "phone": parts[1],
                        "city": parts[2]
                    })
            return customers
    except FileNotFoundError:
        return []

def save_customers(customers):
    """Save customers to file"""
    with open("customers_db.txt", "w") as f:
        for c in customers:
            f.write(c["name"] + " - " + c["phone"] + " - " + c["city"] + "\n")

def show_menu():
    """Display main menu"""
    print("=" * 42)
    print("  SMART AGENT - Week 1 Project")
    print("=" * 42)
    print("  1. Show all customers")
    print("  2. Add new customer")
    print("  3. Search customer")
    print("  4. Send welcome message")
    print("  5. Delete customer")
    print("  6. Save & Exit")
    print("=" * 42)

def show_customers(customers):
    """Display all customers"""
    print("\n  CUSTOMER LIST:")
    print("  " + "-" * 30)
    if not customers:
        print("  No customers found!")
    else:
        for i, c in enumerate(customers, 1):
            print("  " + str(i) + ". " + c["name"] + " | " + c["phone"] + " | " + c["city"])
    print("  " + "-" * 30)
    print("  Total: " + str(len(customers)))

def add_customer(customers):
    """Add a new customer"""
    print("\n  ADD NEW CUSTOMER:")
    name = input("  Name: ")
    phone = input("  Phone: ")
    city = input("  City: ")
    customers.append({"name": name, "phone": phone, "city": city})
    print("  SAVED: " + name)

def search_customer(customers):
    """Search for a customer"""
    name = input("\n  Search name: ")
    found = False
    for c in customers:
        if name.lower() in c["name"].lower():
            print("  FOUND: " + c["name"] + " - " + c["phone"] + " - " + c["city"])
            found = True
    if not found:
        print("  NOT FOUND")

def send_message(customers):
    """Send welcome message to all"""
    if not customers:
        print("\n  No customers to message!")
        return
    print("\n  Sending messages...")
    for c in customers:
        print("  To " + c["name"] + ": Welcome! We are here to help.")
    print("  All messages sent!")

def delete_customer(customers):
    """Delete a customer"""
    name = input("\n  Enter name to delete: ")
    for i in range(len(customers)):
        if customers[i]["name"].lower() == name.lower():
            customers.pop(i)
            print("  DELETED: " + name)
            return
    print("  NOT FOUND")

# ========== MAIN PROGRAM ==========
customers = load_customers()

print("\n" + "=" * 42)
print("  Welcome to Smart Agent v1.0")
print("=" * 42)

while True:
    show_menu()
    choice = input("  Choose (1-6): ")
    
    if choice == "1":
        show_customers(customers)
    elif choice == "2":
        add_customer(customers)
    elif choice == "3":
        search_customer(customers)
    elif choice == "4":
        send_message(customers)
    elif choice == "5":
        delete_customer(customers)
    elif choice == "6":
        save_customers(customers)
        print("\n  SAVED. Goodbye!")
        print("=" * 42)
        break
    else:
        print("\n  Invalid choice! Try again.")

