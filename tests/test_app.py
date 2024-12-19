import unittest
from lib.db.models import Customer, Address, Order
from lib.db import initialize_database, create_customer, create_address, create_order, read_customers, read_addresses, read_orders
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db import Base

class TestDatabaseOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the in-memory SQLite database for testing
        cls.engine = create_engine('sqlite:///test_food_delivery.db', echo=True)
        Base.metadata.create_all(cls.engine)
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        Base.metadata.drop_all(cls.engine)

    def test_create_customer(self):
        # Create customer using the helper function
        create_customer(self.session, 'John Doe', '1234567890')
        customers = read_customers(self.session)
        self.assertEqual(len(customers), 1)
        self.assertEqual(customers[0][1], 'John Doe')

    def test_create_address(self):
        # Create customer first
        create_customer(self.session, 'Jane Doe', '0987654321')
        # Now create an address
        create_address(self.session, 1, '123 Elm Street')
        addresses = read_addresses(self.session)
        self.assertEqual(len(addresses), 1)
        self.assertEqual(addresses[0][2], '123 Elm Street')

    def test_create_order(self):
        # Create customer first
        create_customer(self.session, 'John Smith', '1122334455')
        # Create an order for the customer
        create_order(self.session, 1, 'Pizza', 2, 15.0)
        orders = read_orders(self.session)
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0][2], 'Pizza')

    def test_read_customers(self):
        create_customer(self.session, 'Emily', '5566778899')
        customers = read_customers(self.session)
        self.assertGreater(len(customers), 0)

    def test_read_addresses(self):
        create_customer(self.session, 'Michael', '6677889900')
        create_address(self.session, 1, '456 Oak Avenue')
        addresses = read_addresses(self.session)
        self.assertGreater(len(addresses), 0)

    def test_read_orders(self):
        create_customer(self.session, 'Anna', '2233445566')
        create_order(self.session, 1, 'Burger', 1, 5.0)
        orders = read_orders(self.session)
        self.assertGreater(len(orders), 0)

if __name__ == '__main__':
    unittest.main()
