class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def alterarLados(self, base, altura):
        self.base = base
        self.altura = altura

    def mostrarLados(self):
        return 'Base: {} - Altura: {}'.format(self.base, self.altura)

    def calculaArea(self):
        return self.base * self.altura

    def calculaPerimetro(self):
        return 2*(self.base + self.altura)

    def __str__(self):
        return '{}x{}'.format(self.base, self.altura)

r = Retangulo(4,6)
print(r)

print(r.mostrarLados())
print(r.calculaArea())
print(r.calculaPerimetro())
r.alterarLados(5,8)

print(r.mostrarLados())