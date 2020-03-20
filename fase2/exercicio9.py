numeros = []

for i in range(3):
    numeros.append(float(input('Digite o valor {}: '.format(i+1))))

for i in range(len(numeros)-1):
    if numeros[i] < numeros[i+1]:
        aux = numeros[i]
        numeros[i] = numeros[i+1]
        numeros[i+1] = aux

if numeros[0] < numeros[1]:
        aux = numeros[0]
        numeros[0] = numeros[1]
        numeros[1] = aux

print(numeros)