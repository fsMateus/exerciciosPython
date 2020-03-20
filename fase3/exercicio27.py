qtd_turmas = int(input('informe a quantidade de turmas: '))
soma = 0

for i in range(qtd_turmas):
    qtd_alunos = int(input('digite a quantidade de alunos na turma: '))

    if qtd_alunos < 0 and qtd_alunos > 40:
        print('O numero máximo de alunos permitido é 40')
    else:
        soma += qtd_alunos

media = soma / qtd_turmas
print('A quantidade média de alunos por turma é {:.2f}'.format(media))