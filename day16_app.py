# Day 16 - Smart Agent Project: Flask + SQLite Web CRM
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB_NAME = "agent.db"

def get_db():
    """Open database and allow column names like row['name']"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def dashboard():
    """Show customers and orders on one page"""
    conn = get_db()
    
    # Get all customers
    customers = conn.execute("SELECT * FROM customers").fetchall()
    
    # Get orders with customer names (JOIN)
    orders = conn.execute("""
        SELECT orders.id, customers.name, orders.product, orders.amount, orders.status
        FROM orders
        JOIN customers ON orders.customer_id = customers.id
        ORDER BY orders.id DESC
    """).fetchall()
    
    conn.close()
    return render_template("crm.html", customers=customers, orders=orders)

@app.route("/add_customer", methods=["POST"])
def add_customer():
    """Receive form data and insert new customer"""
    name = request.form["name"]
    phone = request.form["phone"]
    city = request.form["city"]
    
    conn = get_db()
    conn.execute("INSERT INTO customers (name, phone, city) VALUES (?, ?, ?)",
                 (name, phone, city))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/add_order", methods=["POST"])
def add_order():
    """Receive form data and insert new order"""
    customer_id = request.form["customer_id"]
    product = request.form["product"]
    amount = request.form["amount"]
    
    conn = get_db()
    conn.execute("INSERT INTO orders (customer_id, product, amount, status) VALUES (?, ?, ?, ?)",
                 (customer_id, product, amount, "pending"))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    print("=" * 50)
    print("SMART AGENT: Web CRM (Flask + SQLite)")
    print("Open: http://localhost:5000")
    print("=" * 50)
    app.run(host="0.0.0.0", port=5000, debug=True)

