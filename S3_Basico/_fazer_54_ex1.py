"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

digito = input('Digite um número inteiro: ')
entrada = int(digito)

if entrada is not int:
    print('O número não é inteiro')
elif entrada % 2 == 0:
    print('É par')
elif entrada % 2 == 1:
    print('É impar')


