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
  

