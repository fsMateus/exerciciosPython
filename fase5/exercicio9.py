def inversoNumero(n):
    aux = str(n)
    msg = ''
    for i in range(len(aux)):
        msg += '{}'.format(aux[(len(aux)-1)-i])

    print(msg)


num = int(input('digite o número: '))
inversoNumero(num)