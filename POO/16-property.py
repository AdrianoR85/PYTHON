class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, new_name):
    if not isinstance(new_name, str):
      raise TypeError("Name must be a string")
    self._name = new_name
    
    
person = Person('Lara', 32)
print(vars(person))