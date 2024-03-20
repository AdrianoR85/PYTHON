class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price
  
  def discount(self, per):
    value_discount = self.price * (per / 100)
    print(f"Price with {per}% off: {self.price - value_discount}")
  
  def __str__(self):
    return f'Name: {self.name}\nPrice: ${self.price}'
  
xbox = Product("Samsung", 4500)
print(xbox)
xbox.discount(10)