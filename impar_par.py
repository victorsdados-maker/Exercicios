
# Exercício: Escreva um programa que solicite ao usuário um número inteiro e determine se ele é par ou ímpar. O programa deve exibir "Par" se o número for par e "Ímpar" se o número for ímpar.
# A diversas formas de fazer,mas o exercício pediu algo extremamente simples então não vamos complicar.
# A solução mais simples que consegui é a seguinte:

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("Par")   
else:
    print("Ímpar") 