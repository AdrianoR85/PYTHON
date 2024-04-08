"""
1- Criando uma Classe Pessoa:
Defina uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie objetos dessa classe e imprima seus atributos.
"""

class Person:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
    
  @property
  def name(self):
    return self.__name
  
  @name.setter
  def name(self, new_name):
    if isinstance(new_name, str) and len(new_name) > 2:
      self.__name = new_name
    else:
      raise ValueError('Name not is valid!')
    
  @property
  def age(self):
    return self.__age
  
  @age.setter
  def age(self, new_age):
    if isinstance(new_age, int) and new_age > 0:
      self.__age = new_age
    else:
      raise ValueError('Age must be an integer greater than 0')
    
  def __str__(self):
    return f'Nome: {self.name}\nIdade: {self.age}\n'
  
p1 = Person('Pedro', 20)
p2 = Person('Lara', 25)
p3 = Person('Triss', 30)

print(p1)
print(p2)
print(p3)

print('-' * 30)
p1.name = 'Pedro Luis'
p2.name = 'Lara Croft'
p3.name = 'Triss Merigold'
print(p1)
print(p2)
print(p3)