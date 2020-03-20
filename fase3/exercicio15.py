f = [1,1]
n = int(input('Informe a quantidade de termos da sequencia: '))
i = 0

while n > len(f):
    f.append(f[i] + f[i+1])
    i += 1

print('A sequencia fibonacci de {}: {}'.format(n, f))
