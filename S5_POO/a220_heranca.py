class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_da_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)
    
class Cliente(Pessoa):
    ...
class Aluno(Pessoa):
    ...

c1 = Cliente('Juliano', 'Sobroza')
c1.falar_nome_da_classe()
a1 = Aluno('Jucimara', 'Souza')
a1.falar_nome_da_classe()

