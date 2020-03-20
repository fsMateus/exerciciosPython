nome = input('digite seu nome: ')

for i in range(1, len(nome)+1):
    msg = ''
    for j in range(i):
        msg += '{}'.format(nome[j].upper())

    print(msg)