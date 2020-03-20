a = float(input('digite o valor de A: '))

if a == 0:
    print('Não é uma equação do segundo grau')
else:
    b = float(input('digite o valor de B: '))
    c = float(input('digite o valor de C: '))

    delta = (b**2) - (4*a*c)
    if delta < 0:
        print('A equação não possui raizes reais')
    elif delta == 0:
        raiz = delta**(1/2)
        x = (-b + raiz) / (2*a)
        print(' a raiz da equação é {}'.format(x))
    else:
        raiz = delta**(1/2)
        x1 = (-b + raiz) / (2*a)
        x2 = (-b - raiz) / (2*a)
        print('as raizes da equação são x1 = {} e x2 = {}'.format(x1, x2))