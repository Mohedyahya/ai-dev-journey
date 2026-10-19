print("="*40)

print("cards ")
print("="*40)

cust = {
    "name":"ali",
    "phone":"776345384",
    "city":"sanaa",
    "order":3
}
print("="*40)

print("name",cust["name"])
print("phone",cust["phone"])
print("city",cust["city"])
print("order",cust["order"])
print("="*40)

cust["order"] = 4
print("new order",cust["order"])

cust["email"] = "ali@gmail.com"
print("email",cust["email"])
print("="*40)
 
custs = [
    {"name":"ali","phone":"7711111111","city": "snaaa"},
    {"name":"ali2","phone":"7711111111","city": "snaaa"},
    {"name":"ali3","phone":"7711111111","city": "snaaa"}
]

print("="*40)

for person in custs:
    print(person["name"],"from",person["city"],"-",person["phone"])

print("="*40)



