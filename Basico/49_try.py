#49. Introdução ao try e except para capturar erros (exceptions)

"""
try/except
try-> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

"""
print('ju')
print("br")
int('lhano') #ValueError: invalid literal for int() with base 10: 'lhano'
"""

"""
numero_float = float(input('Digite o numero para eu dobrar: '))
print(f'O dobro de {numero_float:.0f} é {numero_float*2:.0f}')
"""

#função .isdigit vai retornar um boleano True se o usuario digitar
# apenas números e False se digitar outra coisa
numero_str = input(
    'Digite um numero: '
)
try:
    numero_float = float(numero_str)
    print('Float: ', numero_float)
    print('STR: ', numero_str)
    print(f'O dobro de {numero_str} é {numero_float*2:.2f}')

except:
    print('Isso não é um número')




