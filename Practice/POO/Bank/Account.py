from random import randint

class Account:
  def __init__(self, balance=0.00):
     self.__account_number = str(randint(1000000000, 9999999999))
     self.__balance = float(balance)
  
  @property   
  def balance(self):
    return self.__balance
  
  @property
  def account_number(self):
    return self.__account_number
  
  @balance.setter
  def balance(self, new_balance):
    self.__balance = float(new_balance)
    

# 6594932659 - 600
# 8673573743 - 450
# 3115466757 - 250