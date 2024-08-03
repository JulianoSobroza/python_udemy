"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> - Esqueda
< - Direita
^ - Centro
Sinal -+ ou -
Ex.: 0>-100.1f
Conversion flags - !r !s !a (metodos repr, str, ask)
"""
variavel = " ABCD "
print(f'{variavel}.')           #isso se chama pad
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:&^10}.')  
