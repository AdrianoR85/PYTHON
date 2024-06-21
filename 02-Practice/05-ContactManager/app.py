from Contact import Contact
from ContactManager import ContactManager
import os
def show_menu():
  print("Choose one option below:")
  print("""
  [1] - Add new contact
  [2] - Delete a contact
  [3] - List all contacts
  [4] - Exit""")
  
  
def app():
  cm = ContactManager()
  show_menu()
  while True:
    option = input("\nEnter option: ")
    
    if option == "1":
     name = input("Enter name: ")
     email = input("Enter email: ")
     phone = input("Enter phone: ")
     
     contact = Contact(name, email, phone)
     cm.add_contact(contact)
    elif option == "2":
      print("\n=====Remove contact=====")
      name = input("Enter name: ")
      cm.remove_contact(name)
    elif option == "3":
      print("\n=====Show contact=====")
      cm.display_contact()
    elif option == "4":
      break
    else:
      print("Invalid option")
    show_menu()

if __name__ == "__main__":
  app()