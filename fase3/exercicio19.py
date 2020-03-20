numeros = []
n = 0
print('informe os valores do conjunto (entre 0 e 1000). Para sair digite -1')

while n != -1:
    n = int(input('Digite o valor: '))
    if n > 0 and n < 1000:
        numeros.append(n)
    elif n == -1:
        break
    else:
        print('Valor fora do limite. (entre 0 e 1000)')

maior = numeros[0]
menor = numeros[0]
soma = 0

for i in range(len(numeros)):
    maior = numeros[i] if numeros[i] > maior else maior
    menor = numeros[i] if numeros[i] < menor else menor
    soma += numeros[i]

print('Conjunto: {}\nO menor valor é {}, o maior é {} e a soma de todos os valores é {}'.format(numeros, menor, maior, soma))