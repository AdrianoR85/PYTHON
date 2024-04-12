from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from connection import Base

class Address(Base):
  __tablename__ = 'address'
  
  id = Column(Integer, primary_key=TRUE)
  street = Column(String(100))
  number = Column(Integer(4))
  city = Column(String(50))
  state = Column(String(50))
  customer_id = Column(Integer, ForeignKey('customer.id'))
  customer = relationship('Customer', back_populates='customer')