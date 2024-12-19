import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Customer, Address, Order
from lib.customers import create_customer, read_customers, update_customer, delete_customer
from lib.orders import create_order, read_orders
from lib.addresses import create_address, read_addresses

class TestDatabaseOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db_name = 'test_food_delivery.db'  # Use a separate DB for testing
        cls.engine = create_engine(f'sqlite:///{cls.db_name}', echo=True)
        Base.metadata.create_all(cls.engine)  # Create tables using SQLAlchemy

        # Create a session maker and bind it to the engine
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

    @classmethod
    def tearDownClass(cls):
        # Drop the tables after tests
        Base.metadata.drop_all(cls.engine)
        cls.session.close()

    def test_create_customer(self):
        create_customer('John Doe', '1234567890')
        customers = read_customers()
        self.assertEqual(len(customers), 1)
        self.assertEqual(customers[0].name, 'John Doe')

    def test_create_address(self):
        create_customer('Jane Doe', '0987654321')
        create_address(1, '123 Elm Street')
        addresses = read_addresses()
        self.assertEqual(len(addresses), 1)
        self.assertEqual(addresses[0].address, '123 Elm Street')

    def test_create_order(self):
        create_customer('John Smith', '1122334455')
        create_order(1, 'Pizza', 2, 15.0)
        orders = read_orders()
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0].item_name, 'Pizza')

    def test_read_customers(self):
        create_customer('Emily', '5566778899')
        customers = read_customers()
        self.assertGreater(len(customers), 0)

    def test_read_addresses(self):
        create_customer('Michael', '6677889900')
        create_address(1, '456 Oak Avenue')
        addresses = read_addresses()
        self.assertGreater(len(addresses), 0)

    def test_read_orders(self):
        create_customer('Anna', '2233445566')
        create_order(1, 'Burger', 1, 5.0)
        orders = read_orders()
        self.assertGreater(len(orders), 0)

    def test_update_customer(self):
        create_customer('Old Name', '1112223333')
        customers = read_customers()
        customer_id = customers[0].id
        update_customer(customer_id, 'New Name', '4445556666')
        updated_customer = read_customers()
        self.assertEqual(updated_customer[0].name, 'New Name')

    def test_delete_customer(self):
        create_customer('Delete Me', '9998887777')
        customers = read_customers()
        customer_id = customers[0].id
        delete_customer(customer_id)
        customers_after_delete = read_customers()
        self.assertEqual(len(customers_after_delete), 0)

if __name__ == '__main__':
    unittest.main()
