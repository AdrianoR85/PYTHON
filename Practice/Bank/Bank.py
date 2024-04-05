import Accounts
import People
from typing import Optional

class Bank:
  def __init__(
    self, 
    branches: Optional[list[int]] = None, 
    clients: Optional[list[People.Person]] = None, 
    accounts: Optional[list[Accounts.Account]] = None
    ):
    self.branches = branches or []
    self.clients = clients or []
    self.accounts = accounts or []
  
  def _check_branck(self, account):
    if account.branch in self.branches:
      return True
    return False
  
  def _check_client(self, client):
    if client in self.clients:
      return True
    return False
    
  def _check_account(self, account):
    if account in self.accounts:
      return True
    return False
  
  def authenticate(self, client, account):
    return self._check_branck(account) and \
      self._check_client(client) and \
      self._check_account(account)
      
  def __repr__(self) -> str:
    class_name = type(self).__name__
    attrs = f'branch={self.branches!r}\naccount={self.accounts!r}\nclients={self.clients!r}'
    return f'{class_name} {attrs}'


if __name__ == '__main__':
    c1 = People.Client('Luiz', 30)
    cc1 = Accounts.Current_Account(111, 222, 0, 0)
    c1.account = cc1
    c2 = People.Client('Maria', 18)
    cp1 = Accounts.Savings_Account(112, 223, 100)
    c2.account = cp1
    bank = Bank()
    bank.clients.extend([c1, c2])
    bank.accounts.extend([cc1, cp1])
    bank.branches.extend([111, 222])

    if bank.authenticate(c1, cc1):
        cc1.deposit(10)
        c1.account.withdraw(100)
        print(c1.account)