s = '1'
soma = 1
n = int(input('Digite o número de termos: '))

for i in range(2, n+1):    
    s += ' + {}/{}'.format(1, i)
    soma += 1/i

print('S = {}\nS = {:.2f}'.format(s, soma))