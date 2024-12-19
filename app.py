# app.py

from lib.customers import create_customer, read_customers, update_customer, delete_customer
from lib.orders import create_order, read_orders
from lib.addresses import create_address, read_addresses
import sqlite3

def main_menu():
    while True:
        print("\nFood Delivery App - Menu")
        print("1. Manage Customers")
        print("2. Manage Addresses")
        print("3. Manage Orders")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n1. Add Customer")
            print("2. View Customers")
            print("3. Update Customer")
            print("4. Delete Customer")
            sub_choice = input("Choose: ")
            if sub_choice == "1":
                create_customer(input("Name: "), input("Phone: "))
            elif sub_choice == "2":
                customers = read_customers()
                for customer in customers:
                    print(customer)
            elif sub_choice == "3":
                update_customer(int(input("Customer ID: ")), input("New Name: "), input("New Phone: "))
            elif sub_choice == "4":
                delete_customer(int(input("Customer ID: ")))
        elif choice == "2":
            print("\n1. Add Address")
            print("2. View Addresses")
            sub_choice = input("Choose: ")
            if sub_choice == "1":
                create_address(int(input("Customer ID: ")), input("Address: "))
            elif sub_choice == "2":
                addresses = read_addresses()
                for address in addresses:
                    print(address)
        elif choice == "3":
            print("\n1. Place Order")
            print("2. View Orders")
            sub_choice = input("Choose: ")
            if sub_choice == "1":
                order = {
                    "user_id": int(input("Customer ID: ")),
                    "items": [{"item_id": int(input("Item ID: ")), "quantity": int(input("Quantity: ")), "price": float(input("Price: "))}]
                }
                create_order(order)
            elif sub_choice == "2":
                orders = read_orders()
                for order in orders:
                    print(order)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()