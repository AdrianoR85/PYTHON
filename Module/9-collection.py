from collections import Counter, namedtuple, deque
from operator import itemgetter

fruits  = ['apple','orange','strawberry','pineapple', 'orange']
print(Counter(fruits))

# Utilizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game('FIFA23', 90.50, 8.5)
g2 = game('Resident Evil 4 Remake', 300, 10)
print(g1)
print(g2)

# Ordenando dicionario

students = {"Lara": 23, "Triss":26, "Ciri":22, "Yennefer":25}
a = sorted(students.items(), key=itemgetter(0))
print(students)
print(a)

# Utilizando fila ambas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)
deq.append(90)
print(deq)
deq.popleft()
print(deq)
deq.pop()
print(deq)