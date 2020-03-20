qtd_eleitores = int(input('digite a quantidade de eleitores: '))
a = 0
b = 0
c = 0

for i in range(qtd_eleitores):
    voto = input('Vote em um candidato: A B C ')

    if voto.lower() == 'a':
        a += 1
    elif voto.lower() == 'b':
        b += 1
    elif voto.lower() == 'c':
        c += 1
    else:
        print('voto inválido')

print('O candidato A obteve {} votos\nO candidato B obteve {} votos\nO candidato C obteve {} votos'.format(a, b, c))