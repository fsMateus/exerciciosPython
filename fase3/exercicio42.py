intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
print('Digite um valor negativo para encerrar a execução.')
while True:
    n = int(input('Digite o número: '))

    if n < 0:
        break
    elif n <= 25:
        intervalo1 += 1
    elif n <= 50:
        intervalo2 += 1
    elif n <= 75:
        intervalo3 += 1
    elif n <= 100:
        intervalo4 += 1
    
print('{} entre[0-25], {} entre[26-50], {} entre[51-75], {} entre[76-100]'.format(intervalo1, intervalo2, intervalo3, intervalo4))