import os
def add_contact():
  name = input('Enter your name: ')
  address = input('Enter your address: ')
  phone = input('Enter your phone number: ')
  
  contact = f'Name: {name} \nAddress: {address} \nPhone: {phone}\n'
  
  with open("contacts.txt", "a", encoding="utf-8") as file:
    file.write(contact)

def show_contacts():
  if not os.path.exists("contacts.txt"):
    print("File not found")
    return
  
  with open("contacts.txt", "r", encoding="utf-8") as file:
    contacts = file.read()
  print("Contact List")
  print(contacts)
  
def delete_contacts():
  if not os.path.exists("contacts.txt"):
    print("File not found")
    return
  
  with open("contacts.txt", "w", encoding="utf-8") as file:
    file.write("")