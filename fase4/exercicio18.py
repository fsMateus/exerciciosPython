print('Quem foi o melhor jogador?')
contadores = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

while True:
    num = int(input('Número do jogador (0=fim): '))
    if num == 0:
        break
    elif num < 0 or num > 23:
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
    else:
        contadores[num-1] += 1

total = sum(contadores)
print('\nResultado da Votação:\nForam computados {} votos.\nJogador Votos   %'.format(total))
for i in range(len(contadores)):
    if contadores[i] > 0:
        print('{}\t{}\t{:.1f}%'.format(i+1, contadores[i], (contadores[i]/total)*100))

pos = contadores.index(max(contadores))
print('O melhor jogador foi o número {}, com {} votos, correspondendo a {:.2f}% no total de votos'.format(pos+1, contadores[pos], (contadores[pos]/total)*100))