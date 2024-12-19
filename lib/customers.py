import sqlite3

def create_customer(name, phone):
    connection = sqlite3.connect("food_delivery.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Customers (name, phone) VALUES (?, ?)", (name, phone))
    connection.commit()
    connection.close()
    print("Customer added successfully!")

def read_customers():
    connection = sqlite3.connect("food_delivery.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Customers")
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        print(row)

def update_customer(customer_id, new_name, new_phone):
    connection = sqlite3.connect("food_delivery.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE Customers SET name = ?, phone = ? WHERE id = ?", (new_name, new_phone, customer_id))
    connection.commit()
    connection.close()
    print("Customer updated successfully!")

def delete_customer(customer_id):
    connection = sqlite3.connect("food_delivery.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Customers WHERE id = ?", (customer_id,))
    connection.commit()
    connection.close()
    print("Customer deleted successfully!")