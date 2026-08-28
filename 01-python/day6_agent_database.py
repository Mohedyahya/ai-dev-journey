# Day 6 - Smart Agent Project: Text Database
print("=" * 50)
print("SMART AGENT: Customer Database")
print("=" * 50)

def save_customer(name, phone):
    file = open("agent_customers.txt", "a")
    file.write(name + " - " + phone + "\n")
    file.close()
    print("SAVED: " + name)

def show_all_customers():
    print("\nCUSTOMER LIST:")
    print("-" * 30)
    try:
        file = open("agent_customers.txt", "r")
        number = 1
        for line in file:
            print(str(number) + ". " + line.strip())
            number += 1
        file.close()
        print("-" * 30)
        print("Total: " + str(number - 1))
    except FileNotFoundError:
        print("No customers yet!")

def search_customer(name):
    print("\nSEARCH: " + name)
    try:
        file = open("agent_customers.txt", "r")
        found = False
        for line in file:
            if name in line:
                print("FOUND: " + line.strip())
                found = True
        file.close()
        if not found:
            print("NOT FOUND")
    except FileNotFoundError:
        print("No file!")

# Test
save_customer("Ali", "77111111")
save_customer("Mohammed", "77222222")
save_customer("Fatima", "77333333")

show_all_customers()
search_customer("Mohammed")
search_customer("Khalid")

print("\n" + "=" * 50)
print("AGENT: Day 6 complete!")
print("=" * 50)

