def factorial(num):
  if num == 1:
    return 1
  else:
    return num * factorial(num - 1)
  
number = int(input('Enter a number: '))
print(f'The factorial of the number {number} is: {factorial(number)}')

def total_sum(num):
  if num == 1:
    return 1
  else:
    return num + total_sum(num - 1)
  
number = int(input('Enter a number: '))
print(f'The sum of the numbers from 1 to {number} is: {total_sum(number)}')