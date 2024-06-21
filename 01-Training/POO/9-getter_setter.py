class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.__salary = salary
  
  # Methods for getting the name of the employee
  def get_salary(self):
    return self.__salary
  
  # Methods for setting tha salary of the employee
  def set_salary(self, value):
    self.__salary = value
    
  def show(self):
    print(f"Name: {self.name} - Salary: {self.__salary}")
    
triss = Employee('Triss', 5000)
lara = Employee('Lara', 4000)
triss.show()

triss.set_salary = 6000
triss.show()