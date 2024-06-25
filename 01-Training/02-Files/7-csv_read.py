import csv

courses = []

with open('data/courses.csv', 'r', encoding='utf-8') as file:
  reader = csv.DictReader(file)
  for row in reader:
    courses.append({ "language":row["language"], "category":row["category"] })
    
for course in courses:
  print(f'{course["language"]}: {course["category"]}')