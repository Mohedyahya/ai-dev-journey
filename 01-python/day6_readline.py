# Day 6 - Read customers line by line
print("=" * 40)
print("AGENT: Customer List")
print("=" * 40)

file = open("customers.txt", "r")
number = 1

for line in file:
    print(str(number) + ". " + line.strip())
    number = number + 1

file.close()

print("=" * 40)
print("Total: " + str(number - 1))
print("=" * 40)

