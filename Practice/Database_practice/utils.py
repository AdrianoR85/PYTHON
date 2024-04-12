from Customer import Customer
from connection import Base, engine, session

Base.metadata.create_all(engine)

customer = Customer()
session.add(customer)
session.commit()
def create_customer():