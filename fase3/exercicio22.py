num = int(input('digite um numero: '))
cont = 0
divisiveis = []

for i in range(1, num+1):
    if num % i == 0:
        cont += 1
        divisiveis.append(i)

if cont == 2:
    print('{} é um número primo'.format(num))
else:
    print('{} não é um número primo. Ele é divisivel por {}'.format(num, divisiveis))