"""
2- Calculadora Simples:
Crie uma classe chamada Calculadora. Ela deve ter métodos para adição, subtração, multiplicação e divisão. Teste a classe criando instâncias e realizando operações matemáticas.
"""
class Calculator:
  
  def somar(self ,num1, num2):
    return num1 + num2
  
  def subtract(self, num1, num2):
    return num1 - num2
  
  def multiply(self, num1, num2):
    return num1 * num2
  
  def divide(self, num1, num2):
    if num2 == 0:
      return 'Division by zero is not possible'
    return num1 / num2
  
calc = Calculator()
sum1 = calc.somar(1, 2)
sub = calc.subtract(10, 5)
mult = calc.multiply(3, 5)
div = calc.divide(25, 0)
print(sum1)
print(sub)
print(mult)
print(div)