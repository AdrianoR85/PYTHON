from Contact import Contact

class ContactManager:
  def __init__(self):
    self.__contacts = []
    
  def add_contact(self, contact):
    self.__contacts.append(contact)
    
  def remove_contact(self, name):
    for contact in self.__contacts:
      if contact.name.lower() == name.lower():
        self.__contacts.remove(contact)
        print("Contact removed successfully\n")
        break
    print("Contact not found\n")
  
  def display_contact(self):
    if not self.__contacts:
      print("No Contact\n")
    else:
      for contact in self.__contacts:
        print(contact)
        print('-' * 20)
    