notas = []
n = 0
soma = 0
print('informe os valores. Para sair digite -1')

while n != -1:
    n = float(input('Digite o valor: '))    
    notas.append(n)

    if n == -1:
        break
    
for i in range(len(notas)):
    soma += notas[i]

print('A média das notas é {:.2f}'.format(soma/len(notas)))