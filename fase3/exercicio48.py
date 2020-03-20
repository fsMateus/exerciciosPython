num = int(input('digite o número: '))

if num >= 0:
    aux = str(num)
    invertido = ''
    for i in range(len(aux)):
        invertido += aux[(len(aux)-1)-i]

    print('=> %s' % invertido)
else:
    print('Valor deve ser positivo.')