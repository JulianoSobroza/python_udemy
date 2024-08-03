lista = ['Mariana', 'Isabela', 'Juliana']
cont = 1;

for i in lista:
    nome = 'nome ' + str(cont) + ': '
    cont += 1
    i = nome + i
    print (i)