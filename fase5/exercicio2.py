def imprime(n):
    x = 1
    while x < n+1:
        msg = ''
        for i in range(x):
            msg += '{} '.format(i+1)
        
        print(msg)
        x += 1

n = int(input('digite o valor: '))
imprime(n)