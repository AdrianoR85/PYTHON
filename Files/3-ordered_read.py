names = []

with open("data/names.txt", "r", encoding="utf-8") as file:
  for line in file:
    names.append(line.strip())

for name in sorted(names):
  print(name)