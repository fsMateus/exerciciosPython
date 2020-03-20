nome = input('digite seu nome: ')

for i in range(1, len(nome)+1):
    msg = ''
    for j in range(len(nome)+1-i):
        msg += '{}'.format(nome[j].upper())

    print(msg)