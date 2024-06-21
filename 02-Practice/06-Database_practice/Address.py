from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from connection import Base

class Address(Base):
  __tablename__ = 'address'
  
  id = Column(Integer, primary_key=True)
  street = Column(String(100))
  number = Column(Integer)
  city = Column(String(50))
  state = Column(String(50))
  customer_id = Column(Integer, ForeignKey('customers.id'))
  customer = relationship('Customer', back_populates='address')
  
  def __init__(self, street:str, number:int, city:str, state:str, customer_id:int):
    self.street = street
    self.number = number
    self.city = city
    self.state = state
    self.customer_id = customer_id