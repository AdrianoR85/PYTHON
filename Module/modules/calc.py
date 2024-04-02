import math
def sum(x, y):
  return x + y

def sub(x, y):
  return x - y

def mult(x, y):
  return x * y

def div(x, y):
  if y == 0: return None
  return (x / y)

def delta(a,b,c,):
  delta = (b**2) - (4*a*c)
  return delta 

def equ2(a, b, c):
  delta = (b**2) - (4*a*c)

  if delta < 0:
    return False
  
  x1 = (-b + (math.sqrt(delta))) / (2*a)
  x2 = (-b - (math.sqrt(delta))) / (2*a)
  result = f'Delta = {delta}\nx1 = {x1}\nx2 = {x2}' 
  return result
  
if __name__ == '__main__':
  a = 1
  b = 3
  c = -10
  
  print(equ2(a, b, c))