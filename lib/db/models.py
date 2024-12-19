from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)

    address = relationship("Address", back_populates="customer", uselist=False)
    orders = relationship("Order", back_populates="customer")

    def __repr__(self):
        return f"<Customer(name={self.name}, phone={self.phone})>"

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), unique=True)
    address = Column(String, nullable=False)

    customer = relationship("Customer", back_populates="address")

    def __repr__(self):
        return f"<Address(customer_id={self.customer_id}, address={self.address})>"

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    customer = relationship("Customer", back_populates="orders")

    def __repr__(self):
        return f"<Order(item_name={self.item_name}, quantity={self.quantity}, price={self.price})>"
