# بسم الله - اليوم 6 من الهاتف

print("=" * 40)
print("الوكيل يعم!")
print("=" * 40)

# حفظ عميل في ملف
file = open("phone_customers.txt", "w")
file.write("علي - 771111111\n")
file.write("فاطمة - 772222222\n")
file.close()

print("✅ تم الحفظ")

# قراءة الملف
file = open("phone_customers.txt", "r")
print(file.read())
file.close()

print("=" * 40)

