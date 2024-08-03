# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor feor considerado falso, a expressão inteira será avaliada naquele valor
# 
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor
# 


"""
entrada = input('E para entrar e S para sair: ')
senha_digitada = input('Senha de 4 dígitos: ')

senha_correta = '9785'

if entrada == 'E' and senha_digitada == senha_correta:
    print('Acesso liberado')
elif entrada == 'E' and senha_digitada != senha_correta:
    print('Senha incorreta')


if entrada == 'S':
    print('Você descontectou-se')

#não consegui fazer o código acima
"""


"""
##Avaliação de curto circuito
# print(True and False and True)
# print(True and 0 and True)
"""


"""
if 0 and 1:
    print(True and 1)
 #O 0 (zero) de 0 and 1 avalia como falsy. O corpo do if não será executado.   
"""
