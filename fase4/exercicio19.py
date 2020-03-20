votos = [0,0,0,0,0,0]
marcas = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']

print('Qual o melhor Sistema Operacional para uso em servidores?')
print('1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro')

while True:
    num = int(input('Número do jogador (0=fim): '))
    if num == 0:
        break
    elif num < 0 or num > 6:
        print('Informe um valor entre 1 e 6 ou 0 para sair!')
    else:
        votos[num-1] += 1

total = sum(votos)
print('Sistema Operacional  Votos   %\n----------\t-----\t----')
for i in range(len(votos)):
    print('{}\t{}\t{:.2f}%'.format(marcas[i], votos[i], (votos[i]/total)*100))

pos = votos.index(max(votos))
print('----------\t-----\t----\nTotal\t{}'.format(total))
print('O Sistema Operacional mais votado foi o {}, com {} votos, correspondendo a {:.2f}% votos'.format(marcas[pos], votos[pos], (votos[pos]/total)*100))