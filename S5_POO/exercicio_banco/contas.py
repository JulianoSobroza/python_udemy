import abc

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
       self.agencia = agencia
       self.conta = conta
       self.saldo = saldo
    
    @abc.abstractmethod
    def sacar(self, valor, msg):...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(Realizado o depósito de R${valor:.2f})')

    def detalhes(self, msg):
        print(f'O seu saldo é R${self.saldo:.2f} {msg}')
        print('')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
    
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'Realizado o saque de R${valor}')
            return self.saldo
        
        print('Saldo insuficiente para realizar a operação')
        self.detalhes(f'SAQUE NEGADO.')

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite =0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'Realizado o saque de R${valor}')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')


if __name__ == '__main__':
    cp1 = ContaPoupanca(111,222,0)
    cp1.sacar(1000)
    cp1.depositar(500)

    cc1 = ContaCorrente(112,223,0)
    cc1.depositar(100)
    cc1.sacar (101)