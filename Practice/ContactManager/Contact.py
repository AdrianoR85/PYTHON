"""
3- Gerenciador de Contatos:
Crie uma classe Contato que represente uma pessoa em uma lista de contatos. Ela deve ter atributos como nome, telefone e email. Em seguida, crie uma classe GerenciadorDeContatos que permita adicionar, remover e listar contatos.
"""
class Contact:
  def __init__(self, name, email, phone ):
   self.name = name
   self.email = email
   self.phone = phone
   
  def __str__(self):
    return f"Name: {self.__name}\nEmail: {self.__email}\nPhone: {self.__phone}"