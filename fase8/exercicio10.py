class BombaCombustivel:

    def __init__(self, tipo, valor, qtd):
        self.tipo = tipo
        self.valorLitro = valor
        self.qtd = qtd

    def abastecerValor(self, valor):
        litros = valor / self.valorLitro
        if self.qtd - litros > 0:
            self.qtd -= litros
            print('%.2f' % litros)
            return litros
        else:
            print('Quantidade de combustivel insuficiente!!')

    def abastecerLitros(self, litros):
        preco = litros * self.valorLitro
        if self.qtd - litros > 0:
            self.qtd -= litros
            print('%.2f' % preco)
            return preco
        else:
            print('Quantidade de combustivel insuficiente!!')

    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor

    def alterarTipo(self, novo_tipo):
        self.tipo = novo_tipo

    def alterarQtdCombustivel(self, qtd):
        self.qtd = qtd

b = BombaCombustivel('Gasolina', 4.70, 100)
b.abastecerLitros(30)
b.abastecerValor(20)