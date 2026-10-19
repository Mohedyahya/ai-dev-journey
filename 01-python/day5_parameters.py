print("="*40)

def greet_cust(name):
    print("Hi" +   name + "!")
    print("glad to help you")

greet_cust("ali")
print("-----")

greet_cust("mohammed")

print("----")

def cal_price(p , q):
    total = p * q 
    print("cost: " + str(p))
    print("how :" + str(q))
    print (" total:" + str(total) + "ry")

cal_price(5000,2)

cal_price(15000,1)

print("-------")

def show_cust(city,phone,name):
    print("cust details")
    print("name" + name)
    print("phone" + phone)
    print("city" + city )

show_cust("sanaa","7777777","ali")

print("-----")

show_cust("aden","771111111","sarah")

print("="*60)

