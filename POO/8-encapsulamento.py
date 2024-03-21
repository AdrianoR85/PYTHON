class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.__salary = salary
  
  
  def show(self):
    print(f"Name: {self.name} - Salary: {self.__salary}")
    
triss = Employee('Triss', 5000)
lara = Employee('Lara', 4000)
triss.show()
lara.show()
triss.__salary = 8000
triss.show()