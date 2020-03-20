nome = input('digite seu nome: ')
aux = ''
for i in range(len(nome)):
    aux += '{}'.format(nome[(len(nome)-1)-i])

print(aux.upper())