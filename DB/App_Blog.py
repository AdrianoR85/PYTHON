from Blog import show_menu, new_user ,new_post, show_posts_and_users 
while True:
  show_menu()
  option = input("Enter option: ")
  if option == '1':
    new_user()
  elif option == '2':
    new_post()
  elif option == '3':
    show_posts_and_users()
  elif option == '4':
    break
  else:
    print('Invalid option\n')