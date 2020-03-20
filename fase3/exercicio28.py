qtd_cds = int(input('informe a quantidade de CDs: '))
soma = 0

for i in range(qtd_cds):
    valor_cd = int(input('digite o preço do CD: '))

    if valor_cd < 0:
        print('O numero máximo de alunos permitido é 40')
    else:
        soma += valor_cd

media = soma / qtd_cds
print('O valor total da coleção é {}, e o valor médio de cada CD é {:.2f}'.format(soma, media))