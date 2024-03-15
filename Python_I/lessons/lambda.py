# 1 - Função de potência de números
power = lambda num: num ** 2
print(power(2))

# 2 - Função de verificar se o número é par 
pair = lambda num: num % 2 == 0
print(pair(6))
print(pair(5))

# 3 - Função que divide um número por outro
divNum = lambda x, y: x / y
print(divNum(5,2))
print(divNum(15,3))

# 4 - Função que inverte uma string
reverse = lambda s: s[::-1]
print(reverse('String'))