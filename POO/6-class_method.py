class Console:
  def __init__(self, name, price):
    self.name = name
    self.price = price
    
  @classmethod
  def from_text(cls, string):
    import re
    item = re.findall("é \w*", string)
    name = item[0][2:]
    price = item[1][2:]
    return cls(name, int(price))
  
wiiu = Console.from_text("Meu video game é Wiiu e o preço é 1000 reais")
xboxOne = Console.from_text("Meu video game é XboxOne e o preço é 4500 reais")

print(wiiu.__dict__)
print(xboxOne.__dict__)
