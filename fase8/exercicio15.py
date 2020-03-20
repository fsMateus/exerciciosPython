class Tamaguchi:

    def __init__(self, nome, fome=0, saude=10, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade        

    def alterarNome(self, nome):
        self.nome = nome

    def alterarFome(self, fome):
        self.fome = fome

    def alterarSaude(self, saude):
        self.saude = saude

    def alterarIdade(self, idade):
        self.idade = idade

    def alimentar(self):
        if self.fome <= 0:
            self.fome = 0
        else:
            self.fome -= 1

    def interacao(self, n):
        if n > 0:
            self.saude += self.saude*0.1
            self.fome += self.fome*0.1
        else:
            self.saude -= self.saude*0.1
            self.fome -= self.fome*0.1
        
        self.humor()

    def humor(self):
        return (self.saude + self.fome) / 2
