from Bank import Bank
from Account import Account

def menu():
  print('========== Bank Menu ==========')
  print("1. Add Account")
  print("2. Deposit")
  print("3. Withdraw")
  print("4. Balance")
  print("5. Exit")

def operation(type_operation, bank):
  account_number = input("Enter Account Number: ")
  amount = input("Enter amount: ")
  response = False
  
  if type_operation.lower() == 'withdraw':
     response = bank.withdraw(account_number, float(amount)) 
  elif type_operation.lower() == 'deposit':
    response = bank.deposit(account_number, float(amount))
    
  if response:
        print("-" * 30)
        print(f"\n{type_operation} Successful\n")
        print(f"Account Number: {account_number}\nBalance: {amount}\n")
  else:
    print(f'{type_operation} Failed!!')
  

if __name__ == "__main__":
  bank = Bank()
  
  while True:
    menu()
    option = input("Enter option: ")
    if option == "1":
      new_acc = Account()
      response = bank.create_new_account(new_acc)
      if not response:
        print("failed to create new account")
        break
      print("-" * 30)
      print("\nNew Account created\n")
      print(f"Account Number: {new_acc.account_number}\nBalance: {new_acc.balance}\n")
    elif option == "2":
      response = operation('deposit', bank)
    elif option == "3":
      response = operation('withdraw', bank)
    elif option == "4":
      account_number = input("Enter Account Number: ")
      balance = bank.get_balance(account_number)
      print(balance)
      if balance is not None:
        print(f"Account Number: {account_number}\nBalance: {balance}\n")
      else:
        print(f"Account Number: {account_number} does not exist\n")
    elif option == "5":
      break
    else:
      print("Invalid option")