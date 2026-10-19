# Day 15 - Smart Agent Project: SQLite CRM Database
import sqlite3

# ========== 1. الاتصال بقاعدة البيانات ==========
# إذا لم يكن الملف موجوداً، ينشئه تلقائياً
conn = sqlite3.connect("agent.db")
cursor = conn.cursor()

# ========== 2. إنشاء جدول العملاء ==========
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        city TEXT
    )
""")

# ========== 3. إنشاء جدول الطلبات ==========
# FOREIGN KEY = يربط الطلب بعميل معين
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        product TEXT,
        amount REAL,
        status TEXT DEFAULT 'pending',
        FOREIGN KEY (customer_id) REFERENCES customers (id)
    )
""")

# ========== 4. حفظ التغييرات ==========
conn.commit()

# ========== 5. إضافة عملاء تجريبيين ==========
customers_data = [
    ("Ali", "77111111", "Sanaa"),
    ("Mohammed", "77222222", "Aden"),
    ("Fatima", "77333333", "Taiz")
]
cursor.executemany("INSERT INTO customers (name, phone, city) VALUES (?, ?, ?)", customers_data)
conn.commit()

# ========== 6. إضافة طلبات تجريبية ==========
orders_data = [
    (1, "Laptop", 1500, "pending"),
    (2, "Phone", 800, "pending"),
    (1, "Mouse", 25, "completed"),
    (3, "Keyboard", 45, "pending")
]
cursor.executemany("INSERT INTO orders (customer_id, product, amount, status) VALUES (?, ?, ?, ?)", orders_data)
conn.commit()

# ========== 7. عرض العملاء ==========
print("=" * 50)
print("CUSTOMERS TABLE")
print("=" * 50)
cursor.execute("SELECT * FROM customers")
for row in cursor.fetchall():
    print("ID:", row[0], "| Name:", row[1], "| Phone:", row[2], "| City:", row[3])

# ========== 8. عرض الطلبات مع اسم العميل (JOIN) ==========
print("\n" + "=" * 50)
print("ORDERS WITH CUSTOMER NAMES (JOIN)")
print("=" * 50)
cursor.execute("""
    SELECT orders.id, customers.name, orders.product, orders.amount, orders.status
    FROM orders
    JOIN customers ON orders.customer_id = customers.id
""")
for row in cursor.fetchall():
    print("Order#", row[0], "| Customer:", row[1], "| Product:", row[2], "| $", row[3], "| Status:", row[4])

# ========== 9. تحديث حالة طلب ==========
cursor.execute("UPDATE orders SET status = 'shipped' WHERE id = 2")
conn.commit()

print("\n" + "=" * 50)
print("AFTER UPDATE - Order #2 status changed to 'shipped'")
print("=" * 50)

# ========== 10. عرض إجمالي المبيعات ==========
cursor.execute("SELECT SUM(amount) FROM orders")
total = cursor.fetchone()[0]
print("Total Sales: $" + str(total))

# ========== 11. إغلاق الاتصال ==========
conn.close()

print("\n" + "=" * 50)
print("AGENT: Day 15 Complete! Database saved to agent.db")
print("=" * 50)

