temperaturas_celsius = '0,10,20,30,40'.split(',')

# função chamada converter_celsius_para_fahrenheit que recebe uma lista de strings
def converter_celsius_para_fahrenheit(temperaturas_celsius):
    temperaturas_fahrenheit = [(float(temp) * (9/5) + 32) for temp in temperaturas_celsius]

    # TODO: Calcule as temperaturas em Fahrenheit para cada temperatura em Celsius convertida para float
    return temperaturas_fahrenheit
# Imprime o resultado das temperaturas convertidas para Fahrenheit.
print(converter_celsius_para_fahrenheit(temperaturas_celsius))