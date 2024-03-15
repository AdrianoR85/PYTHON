km = float(input("How many km do you want to train? "))
price = 0
if km <= 200:
  price = km * 0.50
else:
  price = km * 0.35
  
print(f"The price is R${price:.2f}")