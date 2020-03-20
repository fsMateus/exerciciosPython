c1 = c2 = c3 = c4 = nulos = brancos = 0
nomes = ['Jose', 'Augusto', 'Marcos', 'Antonio', 'Nulo', 'Branco']
for i in range(6):
    print('{} - {}'.format(i+1, nomes[i]))

print('Digite o código que representa seu voto. Digite 0 para sair')
while True:
    voto = int(input('Voto: '))
    if voto == 0:
        break
    elif voto == 1:
        c1 += 1
    elif voto == 2:
        c2 += 1
    elif voto == 3:
        c3 += 1
    elif voto == 4:
        c4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1

total = c1 + c2 + c3 + c4 + nulos + brancos
print('Candidato 1: {} votos\nCandidato 2: {} votos\nCandidato 3: {} votos\nCandidato 4: {} votos\nTotal Nulo: {} votos\nTotal Brancos: {} votos\nPorcentagem Nulo: {:.2f}%\nPorcentagem Branco: {:.2f}%\n'.format(c1, c2, c3, c4, nulos, brancos, (nulos/total)*100, (brancos/total)*100))