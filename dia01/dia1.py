# Desenvolva um programa que peça ao usuário para inserir um número.
# O programa deve então verificar se o número é par ou ímpar e exibir uma mensagem informando o usuário.

valor = input("Digite um número:") 
if int(valor) % 2 == 0:
    print("número inserido é par")
else:
    print("número inserido é impar")