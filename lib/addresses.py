import sqlite3

def create_address(customer_id, address):
    connection = sqlite3.connect("food_delivery.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Addresses (customer_id, address) VALUES (?, ?)", (customer_id, address))
    connection.commit()
    connection.close()
    print("Address added successfully!")

def read_addresses():
    connection = sqlite3.connect("food_delivery.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Addresses")
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        print(row)

def update_address(customer_id, new_address):
    connection = sqlite3.connect("food_delivery.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE Addresses SET address = ? WHERE customer_id = ?", (new_address, customer_id))
    connection.commit()
    connection.close()
    print("Address updated successfully!")

def delete_address(customer_id):
    connection = sqlite3.connect("food_delivery.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Addresses WHERE customer_id = ?", (customer_id,))
    connection.commit()
    connection.close()
    print("Address deleted successfully!")