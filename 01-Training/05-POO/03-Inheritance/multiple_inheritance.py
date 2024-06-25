class Animal:
  def __init__(self, paws_number):
    self.paws_numbers =  paws_number
  
  def __str__(self) -> str:
    return f'This animal has {self.paws_numbers} paws'

class Mammal(Animal):
  def __init__(self, fur_color, **kw):
    self.fur_color = fur_color
    super().__init__(**kw)

class Bird(Animal):
  def __init__(self, beak_color, **kw):
    self.beak_color = beak_color
    super().__init__(**kw)

class Cat(Mammal):
  ...

class Ornithorhynchus(Mammal, Bird):
  ...

cat = Cat(paws_number=4, fur_color='black')
print(cat)

o = Ornithorhynchus(paws_number=4, fur_color='red', beak_color='orange')
print(o)