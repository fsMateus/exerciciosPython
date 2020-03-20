class Tamaguchi:

    def __init__(self, nome, fome, saude, idade):
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

    def getNome(self):
        return self.nome

    def getFome(self):
        return self.fome

    def getSaude(self):
        return self.saude

    def getIdade(self):
        return self.idade

    def humor(self):
        if self.fome * self.saude > 40:
            print('Feliz')
        else:
            print('Triste')

t = Tamaguchi('Fofin', 5, 7, 4)
t.alterarFome(2)
t.alterarSaude(9)
t.humor()