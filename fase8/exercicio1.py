class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, novacor):
        self.cor = novacor

    def mostraCor(self):
        print(self.cor)

    def __str__(self):
        return '{}#{} - {}'.format(self.cor, self.material, self.circunferencia)

bola = Bola('azul', 20, 'borracha')
print(bola)

bola.trocaCor('vermelha')
bola.mostraCor()

print(bola)