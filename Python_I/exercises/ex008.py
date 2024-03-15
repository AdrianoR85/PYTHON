def check_char(string):
  type = {'UpperCase': 0, 'LowerCase': 0}
  for char in string:
    if char.isupper():
      type['UpperCase'] += 1
    elif char.islower():
      type['LowerCase'] += 1
  return type
  
string = input("Enter a string: ")
result = check_char(string)
print(result)