altura = float(input('informe sua altura: '))
sexo = input('informe seu sexo: ')

if sexo == 'm':
    print('seu peso ideal é {}'.format(72.7*altura-58))
else:
    print('seu peso ideal é {}'.format(62.1*altura-44.7))