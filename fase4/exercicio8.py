idades = []
alturas = []

for i in range(5):
    idades.append(int(input('Informe sua idade: ')))
    alturas.append(float(input('Informe sua altura: ')))

idades.reverse()
alturas.reverse()

for i in range(5):
    print('{} - {:.2f}'.format(idades[i], alturas[i]))