import Account

class Person:
  def __init__(self, name: str, age: int) -> None:
    self._name = name
    self._age = age
    
  @property
  def name(self) -> str:
    return self._name
  
  @property
  def age(self) -> int:
    return self._age
  
  @name.setter
  def name(self, name: str):
    self._name = name
    
  @age.setter
  def age(self, age: int):
    self._age = age
    
  def __repr__(self) -> str:
    class_name = type(self).__name__
    attrs = f'name={self._name!r}, age={self._age!r}'
    return f'{class_name} {attrs}'

class Client(Person):
  def __init__(self, name: str, age: int) -> None:
    super().__init__(name, age)
    self.account: Account.Account | None = None


if __name__ == '__main__':
  
  client = Client('John', 30)
  client.account = Account.Current_Account(111, 222, 0, 0)
  print(client)
  print(client.account)
