notas = []
soma = 0
for i in range(2):
    notas.append(float(input('Digite a nota {}: '.format(i+1))))
    soma += notas[i]

media = soma/len(notas)

if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')