age = 20
if age >= 18:
    print("you are an adulat.")
else:
    print("you are minor.")

s = 85
if s >= 90:
    grade = "excellent"
elif s>= 80:
    grade = "very good"
elif s>= 70:
    grade = "good"
elif s>= 60:
    grade = "pass"
else:
    grade = "fail"

print("your score:", s)
print("your grade:" , grade)

print("=" , 40)
user_s = input("enter your score(0-100)")
user_s = int(user_s)

if user_s >= 90:
    print( "excellent")
elif user_s>= 80:
    print( "very good")
elif user_s>= 70:
    print( "good")
elif user_s>= 60:
    print( "pass")
else:
    print( "fail")

print("=" ,40)
print("never give up")

