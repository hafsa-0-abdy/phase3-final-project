from .db import get_session
from .db.models import Order

def create_order(customer_id, item_name, quantity, price):
    session = get_session()
    new_order = Order(customer_id=customer_id, item_name=item_name, quantity=quantity, price=price)
    session.add(new_order)
    session.commit()
    session.close()
    print("Order added successfully!")

def read_orders():
    session = get_session()
    orders = session.query(Order).all()
    session.close()
    for order in orders:
        print(f"{order.id} - {order.customer_id} - {order.item_name} - {order.quantity} - {order.price}")

def update_order(order_id, new_item_name, new_quantity, new_price):
    session = get_session()
    order = session.query(Order).filter(Order.id == order_id).first()
    if order:
        order.item_name = new_item_name
        order.quantity = new_quantity
        order.price = new_price
        session.commit()
        print("Order updated successfully!")
    else:
        print("Order not found!")
    session.close()

def delete_order(order_id):
    session = get_session()
    order = session.query(Order).filter(Order.id == order_id).first()
    if order:
        session.delete(order)
        session.commit()
        print("Order deleted successfully!")
    else:
        print("Order not found!")
    session.close()
