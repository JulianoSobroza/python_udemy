"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = input('Digite seu cpf sem numero e sem ifen: ')
nove_primeiros = [int(digito) for digito in cpf[:9]]
print(nove_primeiros)

cont = 10
soma = 0
for digito in nove_primeiros:
    soma += cont*digito
    cont -= 1
    if cont == 2:
        break

print(f'Soma dos 9 primeiros X contagem: {soma}')
multiplica_10 = soma*10
print(f'Multiplicando {soma} X 10 = {multiplica_10}')
resto11 = multiplica_10 % 11
print(f'Resto {multiplica_10} % 11 = {resto11}') 
resultado = resto11
if resultado > 9:
    resultado = 0

print(f'O primeiro dígito do CPF é: {resultado}')