notas = []

for i in range(4):
    notas.append(float(input('digite sua nota: ')))

print('Notas: {} - Média: {:.2f}'.format(notas, sum(notas)/len(notas)))