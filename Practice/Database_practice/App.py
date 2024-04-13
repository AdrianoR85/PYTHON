from utils import add_customer, data_generator, validate, show_menu, get_all_customers
import os
from time import sleep
def app():
  input_text = ['First Name', 'Last Name', 'Email', 'Street', 'Number', 'City', 'State']
  
  while True:
    show_menu()
    option = input('Enter option: ')
    
    if option == '1':
      data = data_generator(input_text)
      response = validate(data, input_text)

      if len(response) == 0:
        add_customer(data)
        print("Customer added")
        break
      else:
        print('\n-----ERROR:------\n')
        for res in response:
          print(f'{res} is not valid')
        print('\n-----------------\n')
    elif option == '2':
      pass
    elif option == '3':
      get_all_customers(input_text)
    elif option == '4':
      break
    else: 
      print('\nInvalid option\n')
      sleep(1)
      os.system('cls')

if __name__ == '__main__':
  app()