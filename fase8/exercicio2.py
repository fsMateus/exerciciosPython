class Quadrado:

    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def alterarLado(self, lado):
        self.tamanho_lado = lado

    def mostrarLado(self):
        print(self.tamanho_lado)

    def calcularArea(self):
        return self.tamanho_lado**2

q = Quadrado(3)
print(q)
print(q.calcularArea())
q.alterarLado(5)
print(q.calcularArea())