class vehicle:
  def __init__(self, color:str, license_plate:str, heels_numbers:int ) -> None:
    self.color = color
    self.license_platee = license_plate
    self.heels_numbers = heels_numbers
  
  def start_engine(self) -> str:
    print(f'Starting engine')

class motocicle(vehicle):
  ...

class car(vehicle):
  ...

class truck(vehicle):
  def __init__(self, color:str, license_plate:str, heels_numbers:int, loader:bool=False ) -> None:
    super().__init__(color, license_plate, heels_numbers)
    self.loader = loader
  def loaded(self) -> str:
    print(f'The truck {'is' if self.loader else 'is not'} loaded')

moto = motocicle('blue', 'abc-1234', 4)
car1 = car('red', 'abc-3216', 4)
truck1 = truck('green', 'abc-5241', 8, 1)
moto.start_engine()
car1.start_engine()
truck1.start_engine()
truck1.loaded()