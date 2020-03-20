class Carro:

    def __init__(self, consumo, qtd_combustivel=0):
        self.consumo = consumo
        self.combustivel = qtd_combustivel

    def andar(self, distancia):
        self.combustivel -= distancia / self.consumo

    def obterGasolina(self):
        print('%.2f' % self.combustivel)
        return self.combustivel

    def adicionarGasolina(self, qtd):
        self.combustivel += qtd

carro = Carro(15)
carro.adicionarGasolina(20)
carro.andar(100)
carro.obterGasolina()