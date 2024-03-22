from contact import Contact
from contact_book import ContactBook
from time import sleep
import os

def show_menu():
  print("Choose one option below:")
  print("""
  [1] - Add new contact
  [2] - List all contacts
  [3] - Search for a contact
  [4] - Delete a contact
  [5] - Exit
    """)


def header():
  name = "Name"
  Phone = "Phone Number"
  Email = "Email Address"
  
  print(f"\n{name :<10} {Phone :<15} {Email}")
  print('-' * 45)


def main():
  contact_book = ContactBook()
  
  while True:
    show_menu()
    choose = input('> ')
  
    if choose == '1':
      name = input('Enter contact name: ')
      phone = input('Enter contact number: ')
      email = input('Enter contact email: ')
      
      contact = Contact(name, phone, email)
      contact_book.add_contact(contact)
      
      print("\nContact added successfully\n")
    elif choose == '2': # Display the contact
      header()
      contact_book.display_contact()
    elif choose == '3': # Search a contact
      name = input('Enter contact name: ')
      contact_book.search_contact(name)
    elif choose == '4': # Delete a contact
      name = input('Enter contact name to remove: ')
      contact = contact_book.search_contact(name)   
      if contact:
        contact_book.remove_contact(contact)
        print("\nContact deleted successfully\n")
    elif choose == '5':
      break
    else:
      print('Invalid option')
      sleep(.7)
      os.system('cls')
    

if __name__ == '__main__':
  main()