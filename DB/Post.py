from connection_orm import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
  __tablename__ = 'posts'
  
  id = Column(Integer, primary_key=True)
  title = Column(String)
  content = Column(String)
  author_id = Column(Integer, ForeignKey('users.id'))
  author = relationship('User', back_populates='post')
  
  def __init__(self, title:str, content:str, author_id:int):
    self.title = title
    self.content = content
    self.author_id = author_id
    
    