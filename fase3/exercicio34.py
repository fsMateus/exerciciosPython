num = int(input('digite um numero: '))
cont = 0

for i in range(1, num+1):
    if num % i == 0:
        cont += 1

if cont == 2:
    print('{} é um número primo'.format(num))
else:
    print('{} não é um número primo'.format(num))