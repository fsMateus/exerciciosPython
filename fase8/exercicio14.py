class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obterNome(self):
        print(self.nome)
        return self.nome

    def obterSalario(self):
        print('%.2f' % self.salario)
        return self.salario

    def aumentarSalario(self, taxa):
        self.salario += self.salario*taxa

f = Funcionario('Mateus', 1470.50)
f.obterNome()
f.obterSalario()
f.aumentarSalario(0.1)
f.obterSalario()