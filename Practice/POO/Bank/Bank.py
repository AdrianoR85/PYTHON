"""
4- Banco:
Crie uma classe Banco que tenha métodos para adicionar contas bancárias, verificar o saldo e realizar depósitos e saques. Cada conta bancária deve ser uma classe separada com um número de conta único e um saldo inicial.
"""

from Account import Account


class Bank:
    def __init__(self):
      self.accounts = []

    def create_new_account(self, new_account):
        self.accounts.append(new_account)
        return True
    
    def deposit(self, account_number, amount):
      for account in self.accounts:
        if account.account_number == account_number:
          account.balance += amount
          return True
      return False
    
    def get_balance(self, account_number):
      for account in self.accounts:
        if account.account_number == account_number:
          return account.balance
      return None
    
    def withdraw(self, account_number, amount):
      for account in self.accounts:
        if account.account_number == account_number and account.balance >= amount:
          account.balance -= amount
          return True
      return False
    