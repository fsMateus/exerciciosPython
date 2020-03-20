peso = float(input('Digite o peso total de peixes: '))
excesso = peso - 50 if peso > 50 else 0
multa = excesso * 4

if excesso > 0:
    print('O Peso total de peixes é {} quilos, o excesso foi {} quilos, e a multa a ser paga custa R${}'.format(peso, excesso, multa) )
else:
    print('O Peso total de peixes é {} quilos, não houve excesso')    