import os
from dotenv import load_dotenv # type: ignore
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

def get_database_url():
  load_dotenv()
  USER = os.getenv('USER')
  PASSWORD = os.getenv('PASSWORD')
  HOSTNAME = os.getenv('HOSTNAME')
  DATABASE = os.getenv('DATABASE')
  return f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOSTNAME}/{DATABASE}'

DATABASE_URL = get_database_url()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
