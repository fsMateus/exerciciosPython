def qtdDigitos(n):
    aux = str(n)
    return len(aux)

num = int(input('digite um numero: '))
print('O número {} possui {} digitos'.format(num, qtdDigitos(num)))