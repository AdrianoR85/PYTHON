import re

text = "O sol brilha intensamente no céu azul de Joinville."
# Índice inicial e final de palavras
match = re.search(r'O sol', text)
print('Índice inicial ', match.start())
print('Índice final ', match.end())

#Buscando o índice que possui o ponto
site = 'http://python.org/'
match = re.search(r'\.', site)
print(match)

# Buscando uma lista de caracters dentro de uma frase
pattern = "[a-c]"
result = re.findall(pattern, text)
print(text)
print(result)

# Verificando o início de uma string
rule = r'^A'
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']
for p in phrases:
  match = re.match(rule, p)
  if match:
    print(p)

# Verificando o final de uma string
rule_end = r'!$'
phrase = 'O dia está lindo!'
match = re.search(rule_end, phrase)
if match:
  print("Sim, corresponde")
else:
  print("Não corresponde")