from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from connection import Base

class Customer(Base):
  __tablename__ = 'customers'
  
  id = Column(Integer, primary_key=True)
  first_name = Column(String(50))
  last_name = Column(String(50))
  email = Column(String(100))
  address = relationship('Address', back_populates='address')
  
  def __init__(self,first_name:str,last_name:str, email:str):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email

  

  