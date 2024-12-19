import sqlite3

def create_order(customer_id, item_name, quantity, price):
    connection = sqlite3.connect("food_delivery.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Orders (customer_id, item_name, quantity, price) VALUES (?, ?, ?, ?)", 
                   (customer_id, item_name, quantity, price))
    connection.commit()
    connection.close()
    print("Order added successfully!")

def read_orders():
    connection = sqlite3.connect("food_delivery.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Orders")
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        print(row)

def update_order(order_id, new_item_name, new_quantity, new_price):
    connection = sqlite3.connect("food_delivery.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE Orders SET item_name = ?, quantity = ?, price = ? WHERE id = ?", 
                   (new_item_name, new_quantity, new_price, order_id))
    connection.commit()
    connection.close()
    print("Order updated successfully!")

def delete_order(order_id):
    connection = sqlite3.connect("food_delivery.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Orders WHERE id = ?", (order_id,))
    connection.commit()
    connection.close()
    print("Order deleted successfully!")