print('Digite -1 para sair')
# temperaturas = []
qtd = 0
soma = 0
maior = 0
menor = 0

while True:
    temp = float(input('digite a temperatura: '))

    if temp == -1:
        break

    # temperaturas.append(temp)
    soma += temp
    qtd += 1
    if qtd == 1:
        menor = temp
    maior = temp if temp > maior else maior
    menor = temp if temp < menor else menor

media = soma / qtd
# menor = min(temperaturas)
# maior = max(temperaturas)
# media = sum(temperaturas) / len(temperaturas)
print('A menor temperatura é {:.2f}, a maior temperatura é {:.2f} e a temperatura média é {:.2f}'.format(menor, maior, media))