
# Exercício: Escreva um programa que solicite ao usuário um número inteiro e calcule o fatorial desse número usando um laço for e a função range. O programa deve exibir o resultado do fatorial.
# Minha solução:

n=int(input("Digite o número:"))
res = 1
for i in range(1, n + 1):
    res *= i
print(res)  