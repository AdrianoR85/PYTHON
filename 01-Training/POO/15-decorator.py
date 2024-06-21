from decorator import my_decorator, uppercase_decorator, split_string

# Example 01
@my_decorator
def my_function():
  print("Inside of my function")
  
my_function()

# Example 02
@uppercase_decorator
def text():
  return '\nHello, world\n'

print(text())

# Example 03
@split_string
@uppercase_decorator
def example():
  return '\nLearning Python e creating decorators'

print(example())