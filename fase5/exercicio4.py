def valido(a):
    if a > 0:
        return 'P'
    else:
        return 'N'

n = int(input('digite o numero: '))
print(valido(n))