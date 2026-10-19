# ========== المتغيرات ==========
agent_name = "Yahya-Agent"
version = 1.0
is_active = True

# ========== الطباعة ==========
print(f"مرحباً! أنا {agent_name} الإصدار {version}")
print(f"الحالة: {'شغال ✅' if is_active else 'متوقف ❌'}")

# ========== إدخال من المستخدم ==========
user_name = input("\nما اسمك؟ ")
user_age = int(input("كم عمرك؟ "))

# ========== اتخاذ القرار ==========
if user_age >= 18:
    print(f"\nأهلاً بك {user_name}! وصول كامل 🚀")
elif user_age >= 13:
    print(f"\nأهلاً {user_name}! بوضع المتابعة 👀")
else:
    print(f"\nعذراً {user_name}، يحتاج إشراف والد 👨‍👩‍👦")

