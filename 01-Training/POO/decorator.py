def my_decorator(func):
  def wrapper():
    print("Before")
    func()
    print("After")
  return wrapper

def uppercase_decorator(function):
  def wrapper():
    func = function()
    make_uppercase = func.upper()
    return make_uppercase
  return wrapper

def split_string(function):
  def wrapper():
    func = function()
    return func.split()
  return wrapper
