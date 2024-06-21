def even_or_odd(*numbers):
  even = []
  odd = []
  for num in numbers:
    if num % 2 == 0:
      even.append(num)
    else:
      odd.append(num)
  return even, odd
  
even, odd = even_or_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f'Even List: {even}')
print(f'Odd List: {odd}')