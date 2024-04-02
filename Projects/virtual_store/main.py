from Client import Client
from Account import Account


class Main:
  pass


c1 = Client("Lara", "114444-2222")
account = Account(c1.name, '7889456123')

account.deposit(100)
account.withdraw(50)
account.bank_statement()