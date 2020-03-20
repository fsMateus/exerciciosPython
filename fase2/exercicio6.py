numeros = []
numeros.append(float(input('Digite o valor 1: ')))
maior = numeros[0]

for i in range(1,3):
    numeros.append(float(input('Digite o valor {}: '.format(i+1))))
    if maior < numeros[i]:
        maior = numeros[i]

print('O maior valor informado foi {}'.format(maior))