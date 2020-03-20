medias = []
cont = 0
for i in range(10):
    notas = []
    print('Aluno {}'.format(i+1))
    for i in range(4):
        notas.append(float(input('digite sua nota: ')))

    media = sum(notas)/len(notas)
    medias.append(media)
    if media >= 7:
        cont += 1

print('%d alunos com média maior ou igual a 7' % cont)

