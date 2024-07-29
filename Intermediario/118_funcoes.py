# crie funções que duplicam, triplicam e quadriplicam 
# o numero recebido como parâmetro

def criar_multiplicador(multiplocador):
    def multiplicar(numero):
        return numero * multiplocador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

a = 3
b = duplicar(a)
print(duplicar(a))
print (b)