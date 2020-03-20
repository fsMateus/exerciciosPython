class Conta:

    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
        else:
            print('Saldo insuficiente!')

    def __str__(self):
        return '{}#{}'.format(self.nome, self.numero)

c = Conta(102, 'Mateus')
print(c)
c.deposito(55)
c.saque(30)
