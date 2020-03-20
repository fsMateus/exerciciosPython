from random import randrange

n = int(input('defina o tamanho do conjunto: '))
numeros = []

for i in range(n):
    numeros.append(randrange(100))

maior = numeros[0]
menor = numeros[0]
soma = 0

for i in range(n):
    maior = numeros[i] if numeros[i] > maior else maior
    menor = numeros[i] if numeros[i] < menor else menor
    soma += numeros[i]

print('Conjunto: {}\nO menor valor é {}, o maior é {} e a soma de todos os valores é {}'.format(numeros, menor, maior, soma))