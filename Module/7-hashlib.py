import hashlib

# Verifica os algoritmos disponíveis
print(hashlib.algorithms_available)

# Algoritmos disponíveis de acordo com o SO
print(hashlib.algorithms_guaranteed)

# Utilizado o sha256
algorithm = hashlib.sha256()
message = 'A melhor forma de prever o futuro é criá-lo'.encode()
algorithm.update(message)
print(algorithm.hexdigest())

# 4 utilizando o MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())