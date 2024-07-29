# Salve os dados de sua classe em JSON
# Depois crie novamente suas instâncias
# Faça em arquivos separados

import json

CAMINHO_ARQUIVO ='POO/207_classes.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Jorge', 14)
p2 = Pessoa('Nilva', 74)
p3 = Pessoa('Silvinha', 44)

bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)