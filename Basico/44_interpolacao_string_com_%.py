# 44. Interpolação de string com % em Python
"""
Interpolação básica de strings
s - tring
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

"""
nome = 'Luiz'
preco = 1000.95897643
variavel = 'Luiz, o preço total foi R$1000.95'
print (variavel)
"""
# FAzendo o comando acima por interpolação:

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print (variavel)
print ('o hexadecimal de %d é %08x' % (1600, 1600))
