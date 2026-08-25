
print("agent ")
print("="*40)


print("="*40)
customers = [
    {"name":"ali","phone":"7711111111","city": "snaaa","order":5},
    {"name":"ali2","phone":"7711111111","city": "snaaa","order":2},
    {"name":"ali3","phone":"7711111111","city": "snaaa","order":8}
]


print("="*40)

print("="*40)
for i, person in enumerate(customers, 1):
    print(f"{i}. {person['name']} - {person['city']} - ord:{person['order']}")

print("\n search:")
search_name = "allllj"
found = False 



print("="*40)

for person in customers:
    if person["name"] == search_name:
        print(f"find :{person['name']},phone :{person['city']}")
        found = True

if not found:
    print("not found")

print("="*40)

