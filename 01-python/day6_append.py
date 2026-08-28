# Day 6 - Append new customer
print("=" * 40)
print("AGENT: Adding new customer")
print("=" * 40)

file = open("customers.txt", "a")
file.write("Ahmed - 77444444\n")
file.close()

print("SUCCESS: Customer added!")

