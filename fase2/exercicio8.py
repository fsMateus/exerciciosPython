numeros = []
numeros.append(float(input('Digite o valor do produto 1: ')))
menor = numeros[0]
produto = 1

for i in range(1,3):
    numeros.append(float(input('Digite o valor do produto {}: '.format(i+1))))
        
    if menor > numeros[i]:
        menor = numeros[i]
        produto = i+1

print('O produto mais barato é o produto {}, e custa R$ {}'.format(produto, menor))