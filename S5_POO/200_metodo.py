class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando')

c1 = Carro('Chevette')
c1.acelerar()