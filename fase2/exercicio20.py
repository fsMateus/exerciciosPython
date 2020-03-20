notas = []
soma = 0
for i in range(3):
    notas.append(float(input('Digite a nota {}: '.format(i+1))))
    soma += notas[i]

media = soma/len(notas)

if media == 10:
    print('Aprovado com Distinção!\nMédia %.2f' % (media))
elif media >= 7:
    print('Aprovado\nMédia %.2f' % (media))
else:
    print('Reprovado\nMédia %.2f' % (media))