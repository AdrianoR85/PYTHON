class Account:
  def __init__(self, name, number, balance=0.00):
    self._name = name
    self._number = number
    self._balance = balance
    
  @property
  def balance(self):
    return self._balance
    
  def deposit(self, amount):
    self._balance += amount
    
  def withdraw(self, amount):
    if self._balance >= amount:
      self._balance -= amount
    else:
      print("Insufficient funds")  
      
  def bank_statement(self):
    print(f"{self._name}'s account: {self._number}")
    print(f"Balance: {self._balance:0.2f}")