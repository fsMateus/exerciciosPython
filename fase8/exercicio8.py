class Macaco:

    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def verBucho(self):
        print("Alimentos: ")
        for i in self.bucho:
            print(i)
        
    def comer(self, comida):
        self.bucho.append(comida)

    def digerir(self):
        print("...")
        self.verBucho()
        self.bucho = []

    def __str__(self):
        return self.nome

m = Macaco('trovao')
m2 = Macaco('teste')

m.comer('banana')
m2.comer('mandioca')
m.comer('folha')
m2.comer('batata')
m.comer('mel')
m2.comer(m)

m.verBucho()
m2.verBucho()

m2.digerir()