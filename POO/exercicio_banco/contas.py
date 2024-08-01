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
    ...


class ContaCorrente(Conta):
    ...

if __name__ == '__main__':
    cp1 = ContaPoupanca(111,222,0)
    cp1.sacar(1)
    cp1.depositar(500)