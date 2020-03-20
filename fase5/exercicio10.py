from random import randint, random

def lancarDado():
    return randint(2,12)

def jogar(ponto):
    while True:
        dado = lancarDado()
        if dado == 7:
            print('{} - Perdeu'.format(dado))
            break
        elif dado == ponto:
            print('{} - Ganhou'.format(dado))
            break

dado = lancarDado()

if dado == 7 or dado == 11:
    print('{} - Ganhou'.format(dado))
elif dado == 2 or dado == 3 or dado == 12:
    print('{} - Perdeu'.format(dado))
else:
    ponto = dado    
    jogar(ponto)