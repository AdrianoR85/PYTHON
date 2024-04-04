from abc import ABC, abstractmethod

class Account(ABC):
  def __init__(self, branch: int, account_number: int, balance: float = 0) -> None:
    self.branch = branch
    self.account_number = account_number
    self.balance = balance

  @abstractmethod
  def withdraw(self, amount: float) -> float: ...

  def deposit(self, amount: float) -> float:
    self.balance += amount
    self.details(f"(DEPOSIT ${amount})")
    return self.balance

  def details(self, msg: str = "") -> None:
    print(f"Current Balance: ${self.balance} - {msg}")

class Current_Account(Account):
  def __init__(self, branch: int, account_number: int, balance: float=0, limit: float=0 ):
    super().__init__(branch, account_number, balance)
    self.limit = limit

  def withdraw(self, amount) -> float:
    balance_plus_limit = self.balance + self.limit

    if balance_plus_limit >= amount:
        self.balance -= amount
        self.details(f"(WITHDRAW ${amount})")
        return self.balance
    print("Insufficient Funds")
    self.details(f"(WITHDRAW DENIED ${amount})")
    return self.balance

  def __repr__(self) -> str:
    class_name = type(self).__name__
    attrs = f'branch={self.branch!r}, number={self.account_number!r}, balance={self.balance!r}, limit={self.limit!r}'
    return f'{class_name} {attrs}'

class Savings_Account(Account):
  def withdraw(self, amount) -> float:
    if self.balance >= amount:
      self.balance -= amount
      self.details(f"(WITHDRAW ${amount})")
      return self.balance
    print("Insufficient Funds")
    self.details(f"(WITHDRAW DENIED ${amount})")
    return self.balance
  
  def __repr__(self) -> str:
    class_name = type(self).__name__
    attrs = f'branch={self.branch!r}, number={self.account_number!r}, balance={self.balance!r}'
    return f'{class_name} {attrs}'


if __name__ == '__main__':
  sv1 = Savings_Account(111, 222)
  sv1.withdraw(401)
  sv1.deposit(200)
  sv1.withdraw(100)
  print("####")
  ca1 = Current_Account(111, 222, 100)
  ca1.deposit(200)
  ca1.withdraw(100)
  ca1.withdraw(100)
  ca1.withdraw(100)
  ca1.withdraw(1)
