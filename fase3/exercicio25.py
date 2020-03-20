idades = []
soma = 0
print('Para sair digite -1')
while True:
    idade = int(input('Digite sua idade: '))

    if idade == -1:
        break
    elif idade < 0:
        print('valor inválido')
    else:
        idades.append(idade)
        soma += idade

media = soma / len(idades)

if media > 0 and media <= 25:
    print('A turma é jovem')
elif media > 25 and media <= 60:
    print('Turma adulta')
else:
    print('Turma idosa')