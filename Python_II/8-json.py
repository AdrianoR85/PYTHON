import json

# String para Dicionário
person = '{"name": "John", "languages": ["Python", "Java"]}'
person_dic = json.loads(person)
print(person_dic)
print(person_dic['languages'])

# Convertendo dicionário para json
person_json = json.dumps(person_dic)
print(person_json)

# Formatando json
print(json.dumps(person_dic, indent=4, sort_keys=True))

# Salvando json em txt
with open("person.txt", "w") as json_file:
  json.dump(person_dic, json_file,)
  
# Lendo dados externo
