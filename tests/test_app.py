import pytest
from lib.db import init_db, get_session
from lib.db.models import Customer, Order, Address
from lib.customers import create_customer, read_customers
from lib.orders import create_order, read_orders
from lib.addresses import create_address, read_addresses

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    """Set up a fresh database for each test."""
    init_db()
    session = get_session()
    session.query(Order).delete()
    session.query(Address).delete()
    session.query(Customer).delete()
    session.commit()
    session.close()


def test_create_customer():
    create_customer("Alice", "123456789")
    session = get_session()
    customer = session.query(Customer).filter_by(phone="123456789").first()
    session.close()
    assert customer.name == "Alice"


def test_read_customers(capsys):
    create_customer("Alice", "123456789")
    read_customers()
    captured = capsys.readouterr()
    assert "Alice" in captured.out


def test_create_order():
    create_customer("Bob", "987654321")
    session = get_session()
    customer = session.query(Customer).filter_by(phone="987654321").first()
    customer_id = customer.id
    session.close()

    create_order(customer_id, "Burger", 1, 5.99)
    session = get_session()
    order = session.query(Order).filter_by(customer_id=customer_id).first()
    session.close()
    assert order.item_name == "Burger"


def test_read_orders(capsys):
    create_customer("Bob", "987654321")
    session = get_session()
    customer = session.query(Customer).filter_by(phone="987654321").first()
    customer_id = customer.id
    session.close()

    create_order(customer_id, "Burger", 1, 5.99)
    read_orders()
    captured = capsys.readouterr()
    assert "Burger" in captured.out


def test_create_address():
    create_customer("Charlie", "555555555")
    session = get_session()
    customer = session.query(Customer).filter_by(phone="555555555").first()
    customer_id = customer.id
    session.close()

    create_address(customer_id, "123 Main St")
    session = get_session()
    address = session.query(Address).filter_by(customer_id=customer_id).first()
    session.close()
    assert address.address == "123 Main St"


def test_read_addresses(capsys):
    create_customer("Charlie", "555555555")
    session = get_session()
    customer = session.query(Customer).filter_by(phone="555555555").first()
    customer_id = customer.id
    session.close()

    create_address(customer_id, "123 Main St")
    read_addresses()
    captured = capsys.readouterr()
    assert "123 Main St" in captured.out