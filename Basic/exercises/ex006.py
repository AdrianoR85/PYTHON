salary = float(input("Enter your salary: "))
perc_increase = 0.15

if salary > 1250:
  perc_increase = 0.10

increase = salary * perc_increase
print(f"The increase is ${increase}")