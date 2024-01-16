#calculadora
result = 0
num1 = float(input("Digite o 1o número:"))
num2 = float(input("Digite o 2o número:"))
print("Selecione uma operação: ")
print("         1 - adição")
print("         2 - subtração")
print("         3 - divisão")
print("         4 - multiplicação")
oper = input("Qual a operação faremos?")
if oper == "1":
    result = num1 + num2
if oper == "2":
    result = num1 - num2
if oper == "3":
    if num2 == 0:
        result = "divisão por zero!"
    else:
        result = num1 / num2
if oper == "4":
    result = num1 * num2

print("O resultado será ",result)