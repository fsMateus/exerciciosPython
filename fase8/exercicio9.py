class Ponto:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def mostrarPonto(self):
        print('{' + str(self.x) + ', ' + str(self.y) + '}')

    def alterarPonto(self, x, y):
        self.x = x
        self.y = y

class Retangulo:

    def __init__(self, largura, altura, canto):
        self.largura = largura
        self.altura = altura
        self.vertice = canto

    def centroRetangulo(self):
        p = Ponto()
        p.x = self.vertice.x + self.largura/2
        p.y = self.vertice.y + self.altura/2
        
        return p

    def aumentar(self, larg, alt):
        self.largura += larg
        self.altura += alt
    
p1 = Ponto()
box = Retangulo(100, 200, p1)
centro = box.centroRetangulo()
centro.mostrarPonto()

box.aumentar(50, 100)
centro = box.centroRetangulo()
centro.mostrarPonto()