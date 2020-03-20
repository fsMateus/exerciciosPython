numeros = []
numeros.append(float(input('Digite o valor 1: ')))
maior = numeros[0]
menor = numeros[0]

for i in range(1,3):
    numeros.append(float(input('Digite o valor {}: '.format(i+1))))
    if maior < numeros[i]:
        maior = numeros[i]
    
    if menor > numeros[i]:
        menor = numeros[i]

print('O maior valor informado foi {}, e o menor valor foi {}'.format(maior, menor))