class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

    def __str__(self):
        return self.nome

p = Pessoa('Mateus', 24, 58, 1.64)
print(p)
p.envelhecer()
p.engordar(0.7)
p.crescer(0.1)