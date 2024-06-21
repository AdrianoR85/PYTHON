class Animal:
  def __init__(self, name, category):
    self.name = name
    self.category = category

class Fish(Animal):
  race = " "

class Parrots(Animal):
  race = " "
  
class Zoo:
  def __init__(self):
    self.animals_dic = {}
    
  def add_animal(self, animal):
    self.animals_dic[animal.name] = animal.category
    
  def total_of_category(self, category):
    result = 0
    for animal in self.animals_dic.values():
      if animal == category:
        result += 1
    return f"No nosso zoológico temos {result} quantidades de {category}"

zoo = Zoo()
fish = Fish('Sardinha', 'mamíferos')
fish2 = Fish('Bagre', 'mamíferos')
print(vars(fish))

parrots = Parrots('Louro', 'aves')
print(vars(parrots))
zoo.add_animal(fish)
zoo.add_animal(parrots)
zoo.add_animal(fish2)


print(zoo.total_of_category("aves"))
print(zoo.total_of_category("mamíferos"))