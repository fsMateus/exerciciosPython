s = ''
cont = 1
soma = 0
n = int(input('Digite o número de termos: '))

for i in range(1, n+1):
    if i == 1:
        s += '{}/{}'.format(i, cont)
    else:
        s += ' + {}/{}'.format(i, cont)
    cont += 2
    soma += i/cont
print('S = {}\nS = {:.2f}'.format(s, soma))