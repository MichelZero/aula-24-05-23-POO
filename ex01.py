#
# autores: Michel
#
# data: 24/05/2023

# Exercício 1: Faça uma função que receba dois números e retorne qual a soma deles.
# teste a função

# definindo a função somar()
def somar(valor1, valor2):
  total = valor1 + valor2
  return total

# usando a função somar()
num1 = int(input("informe número 1: "))
num2 = int(input("informe número 2: "))
print(f"{num1}+{num2} = {somar(num1, num2)}")
print("fim do programa")