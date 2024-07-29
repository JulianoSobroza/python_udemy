"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome aqui: ') # Entrada 
nletras = len(nome) # Contador de letras

if 2 <= nletras <= 4:
    print('Seu nome é pequeno')
elif 5 <= nletras <= 6:
    print('Seu nome é normal.')
elif nletras > 6:
    print('Seu nome é grande.')
