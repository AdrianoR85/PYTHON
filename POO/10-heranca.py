class Animal:
  name = ''
  height = ''
  color = ''
  
  def eat(self):
    print(f'{self.name} is eating')

class Horse(Animal):
  race = ''
  def escape(self):
    print('The Horse is escaping...')

class Lion(Animal):
  mane = True
  def hunt(self):
    print('The Lion is hunting...')
    
    
h = Horse()
h.name = "Carpeado"
h.height = 300
h.color = "White"
h.escape()
h.eat()

l = Lion()
l.name = "Simba"
l.height = 300
l.color = "Brown"
l.hunt()
l.eat()