n = int(input('digite o valor de n: '))
primos = []

for i in range(1, n+1):
    cont = 0

    for j in range(1, i+1):                
        if i % j == 0:
            cont += 1
    
    if cont == 2:
        primos.append(i)
    
print('Os numeros primos entre 1 e {} são {}'.format(n, primos))