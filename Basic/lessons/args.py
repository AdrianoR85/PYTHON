def sum(*num):
  sum_total = 0
  for n in num:
    sum_total += n
  return sum_total

result = sum(10,7,5)
print(result)

def presentation(**data):
  for key, value in data.items():
    print(f"{key}: {value}")

presentation(name = "Adriano", age = 39, city = "Joinville")
