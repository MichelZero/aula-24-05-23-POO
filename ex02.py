#
# autores: Michel
#
# data: 24/05/2023

# Exercício 1: crie ama classe que seja uma calculadora, com as operações de soma, subtração, multiplicação e divisão.
# teste a classe

# definindo a classe Calculadora()
class Calculadora():
  # definindo os métodos da classe
  # método somar()
  def somar(self, valor1, valor2):
    total = valor1 + valor2
    return total
  
  # método multiplicar()
  def multiplicar(self, valor1, valor2):
    total = valor1 * valor2
    return total
  
  # método dividir()
  def dividir(self, valor1, valor2):
    if valor2 == 0:
      return "não existe divisão por ZERO!"
    else:
      total = valor1 / valor2
      return total
  
  # método subtrair()
  def subtrair(self, valor1, valor2):
    total = valor1 - valor2
    return total
  
  # método potencia()
  def potencia(self, valor1, valor2):
    total = valor1 ** valor2
    return total
  
  # método raiz()
  def raiz(self, valor1):
    total = valor1 ** (1/2)
    return total


# usando o método somar da classe Calculadora
# criar o objeto Calculadora:
calc1 = Calculadora()

# usando o objeto calc:
num1 = int(input("informe número 1: "))
num2 = int(input("informe número 2: "))
# operações
print(f"{num1}+{num2} = {calc1.somar(num1, num2)}")
print(f"{num1}-{num2} = {calc1.subtrair(num1, num2)}")
print(f"{num1}/{num2} = {calc1.dividir(num1, num2)}")
print(f"{num1}*{num2} = {calc1.multiplicar(num1, num2)}")
print(f"{num1}^{num2} = {calc1.potencia(num1, num2)}")
print(f"raiz{num1} = {calc1.raiz(num1)}")

print("fim do programa")

