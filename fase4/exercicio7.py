numeros = [6,9,13,4,7]
soma = 0
mult = 1

for i in numeros:
    soma += i
    mult *= i

print('Soma dos valores: {}\nMultiplicação dos valores: {}\nValores: {}'.format(soma, mult, numeros))