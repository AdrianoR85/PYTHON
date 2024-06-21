class Phone:
  def __init__(self, brand, model_name, price):
    self._brand = brand
    self._model_name = model_name
    self._price = price
  
  def __str__(self):
    return f'Brand: {self._brand}\nModel: {self._model_name}\nPrice: ${self._price}'
  
  @staticmethod
  def make_a_call(phone_num):
    print(f'Calling {phone_num}')

class SmartPhone(Phone):
  def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
    super().__init__(brand, model_name, price)
    
    self.ram = ram
    self.internal_memory = internal_memory
    self.back_camera = back_camera


Motorola = Phone('Motorola', 'G7', 1000)
print(Motorola)
Motorola.make_a_call(998754123)
print(vars(Motorola))
print()

Samsung = SmartPhone('Samsung', 'S23', 4500, '4GB', '128GB', '2.0')
print(Samsung)
Samsung.make_a_call(983204589)
print(vars(Samsung))