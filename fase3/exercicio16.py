f = [1,1]
i = 0
aux = 0

while aux <= 500:
    aux = f[i] + f[i+1]
    f.append(aux)
    i += 1

print('Sequencia fibonacci: {}'.format(f))