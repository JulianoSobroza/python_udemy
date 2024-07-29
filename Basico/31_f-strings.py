nome = 'Juliano'
altura = 1.75
peso = 65
imc = peso/altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura. '  #.2f limitará a duas casas decimais
linha_2 = f'Seu peso é de {peso}Kg. '
linha_3 = f'Seu imc é de {imc:.1f}. '

texto = linha_1 + linha_2 + linha_3

print(texto)

