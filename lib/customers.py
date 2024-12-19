from lib.db import get_session
from lib.db.models import Customer

def create_customer(name, phone):
    session = get_session()
    new_customer = Customer(name=name, phone=phone)
    session.add(new_customer)
    session.commit()
    session.close()
    print("Customer added successfully!")

def read_customers():
    session = get_session()
    customers = session.query(Customer).all()
    session.close()
    for customer in customers:
        print(f"{customer.id} - {customer.name} - {customer.phone}")

def update_customer(customer_id, new_name, new_phone):
    session = get_session()
    customer = session.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        customer.name = new_name
        customer.phone = new_phone
        session.commit()
        print("Customer updated successfully!")
    else:
        print("Customer not found!")
    session.close()

def delete_customer(customer_id):
    session = get_session()
    customer = session.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        session.delete(customer)
        session.commit()
        print("Customer deleted successfully!")
    else:
        print("Customer not found!")
    session.close()
