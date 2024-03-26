name = input('Enter your name: ')

# file = open('name.txt', 'a')
# file.write(f'{name}\n')
# file.close()

with open('data/names.txt', 'a') as file:
  file.write(f'{name}\n')