from Customer import Customer
from Address import Address
from sqlalchemy import Table, MetaData
from connection import Base, engine, session
import re

Base.metadata.create_all(engine)
def show_menu():
  print("\nOptions Menu\n")
  print('1 - New customer')
  print('2 - Search Customer')
  print('3 - Show all Customer')
  print('4 - Exit\n')

def is_email_available(email):
  if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    return True
  else:
    return False

def validate(data_list, text_list):
  error_list = []
  for index, data in enumerate(data_list):
    if text_list[index] == 'Email':
      if not is_email_available(data): 
        error_list.append(text_list[index])
    elif text_list[index] == 'Number':
      if not data.isnumeric():
        error_list.append(text_list[index])
    elif len(data) <2:
      error_list.append(text_list[index])
  return error_list 

def data_generator(text_list):
  data_list = []

  for text in text_list:
    data = input(f"Enter {text}: ")
    data_list.append(data)
      
  return data_list  

def add_customer(data):
  # Create a table of customer
  customer = Customer(data[0], data[1], data[2])
  session.add(customer)
  session.commit()
  
  # Create a table of address
  customer = session.query(Customer).filter_by(email=data[2]).first()
  address = Address(data[3], data[4], data[5], data[6], customer.id)
  session.add(address)
  session.commit()
  
def get_all_customers():
  metadata = MetaData()
  metadata.bind = engine

  # Crie uma instância da view
  nome_da_view = Table('show_data_customer', metadata)
  stmt = nome_da_view.select()

  # Execute a consulta e obtenha os resultados
  results = conn.execute(stmt).fetchall()

  # Iterar sobre os resultados, se necessário
  for row in results:
    print(row)

if __name__ == '__main__':
  input_text = ['First Name', 'Last Name', 'Email', 'Street', 'Number', 'City', 'State']
  get_all_customers()