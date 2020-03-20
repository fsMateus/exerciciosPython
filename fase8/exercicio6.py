class Televisao:

    def __init__(self, canal=0, volume=0):
        self.canal = canal
        self.volume = volume

    def mudarCanal(self, canal):
        if canal > 0 and canal < 30:
            self.canal = canal
        else:
            print('Canal indisponível!')

    def aumentarVolume(self, valor):
        if self.volume + valor > 100:
            self.volume = 100
            print('máximo')
        else:
            self.volume += valor

    def diminuirVolume(self, valor):
        if self.volume - valor < 0:
            self.volume = 0
            print('minimo')
        else:
            self.volume -= valor
        

t = Televisao()
t.mudarCanal(10)
t.aumentarVolume(30)
t.aumentarVolume(50)
t.aumentarVolume(50)