class ContaInvestimento:

    def __init__(self, numero, nome, saldo=0, taxa=0.02):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        self.taxa_juros = taxa

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
        else:
            print('Saldo insuficiente!')

    def obterSaldo(self):
        print('%.2f' % self.saldo)
        return self.saldo

    def addJuros(self):
        self.saldo -= self.taxa_juros*self.saldo

    def __str__(self):
        return '{}#{}'.format(self.nome, self.numero)

conta = ContaInvestimento(130, 'Mateus', 1000, 0.1)
conta.obterSaldo()

for i in range(5):
    conta.addJuros()

conta.obterSaldo()