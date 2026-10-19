# Day 6 - Smart Agent Project: Write customers to file
print("=" * 40)
print("AGENT: Saving customer data to file")
print("=" * 40)

file = open("customers.txt", "w")
file.write("Ali - 77111111\n")
file.write("Mohammed - 77222222\n")
file.write("Fatima - 77333333\n")
file.close()

print("SUCCESS: Saved to customers.txt")
print("=" * 40)

