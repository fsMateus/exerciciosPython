ano = int(input('Informe o ano: '))

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print('O ano é bisexto')
else:
    print('O ano não é bisexto')