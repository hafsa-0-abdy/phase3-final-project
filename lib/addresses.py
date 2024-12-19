from .db import get_session
from .db.models import Address

def create_address(customer_id, address):
    session = get_session()
    new_address = Address(customer_id=customer_id, address=address)
    session.add(new_address)
    session.commit()
    session.close()
    print("Address added successfully!")

def read_addresses():
    session = get_session()
    addresses = session.query(Address).all()
    session.close()
    for address in addresses:
        print(f"{address.id} - {address.customer_id} - {address.address}")

def update_address(customer_id, new_address):
    session = get_session()
    address = session.query(Address).filter(Address.customer_id == customer_id).first()
    if address:
        address.address = new_address
        session.commit()
        print("Address updated successfully!")
    else:
        print("Address not found!")
    session.close()

def delete_address(customer_id):
    session = get_session()
    address = session.query(Address).filter(Address.customer_id == customer_id).first()
    if address:
        session.delete(address)
        session.commit()
        print("Address deleted successfully!")
    else:
        print("Address not found!")
    session.close()
