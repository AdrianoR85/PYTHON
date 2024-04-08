from agenda import add_contact, show_contacts, delete_contacts

def main():
  while True:
    print("Contact Book")
    print("1. Add a new contact")
    print("2. Show the contacts")
    print("3. Remove the contacts")
    print("4. Exit")
    
    opt = input("> ")
    
    if opt == '1':
      add_contact()
    elif opt == '2':
      show_contacts()
    elif opt == '3':
      delete_contacts()
    elif opt == '4':
      break
    else: 
      print("Invalid option")
     
      
if __name__ == '__main__':
  main()