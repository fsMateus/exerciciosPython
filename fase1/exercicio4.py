notas = []
soma = 0

for i in range(4):
    notas.append(float(input('Digite a nota {}: '.format(i+1))))
    soma += notas[i]
    
# media = soma/len(notas)
print('A média obtida é: {}'.format(soma/len(notas)))