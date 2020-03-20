numeros = []
pares = []
impares = []

for i in range(20):
    num = int(input('digite um numero: '))
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(numeros, pares, impares)