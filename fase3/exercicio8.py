numeros = []
for i in range(5):
    numeros.append(int(input('Digite um numero: ')))

soma = 0
for i in numeros:
    soma += i

print('A soma do numeros é {}, e a média é igual a {}'.format(soma, soma/len(numeros)))