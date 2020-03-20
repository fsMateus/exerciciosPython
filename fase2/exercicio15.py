lados = []

for i in range(3):
    lados.append(float(input('Digite o valor do lado {}: '.format(i+1))))
    
if lados[0] + lados[1] > lados[2] or lados[1] + lados[2] > lados[0] or lados[0] + lados[2] > lados[1]:
    print('É um triangulo.')
    if lados[0] == lados[1] and lados[1] == lados[2]:
        print('Equilátero')
    elif lados[0] == lados[1] or lados[1] == lados[2] or lados[0] == lados[2]:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não forma um triangulo!')