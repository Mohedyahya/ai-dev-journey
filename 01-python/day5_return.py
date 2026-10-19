print("-----------------------")

def apply_dis(price,discount):
    dis_amount = price * discount / 100
    final_price = price - dis_amount
    return final_price 

original = 20000
discounted = apply_dis(original,10)
print("cost normal" + str(original))
print("after dis" +str(discounted))


print("----------------------")

def cal_shipping(city):
    if city == "sanaa":
        return 2000
    elif city == "aden":
        return 3000
    else:
        return 2500

city1 = cal_shipping("sanaa")
city2 = cal_shipping("aden")

print("xport sanaa" + str(city1))
print("xport aden" + str(city2))

print("-----------------------")

def cust_rating(order):
    if order >= 10:
        return "VIP cust"
    elif order >= 5:
        return "active cudt"
    else:
        return "good cust"

print("(5  order ) ali :" + cust_rating(5))
print("(12 order) fatma :" + cust_rating(12))
print("(1  order )ahmed: " + cust_rating(1))

print("="*60)
