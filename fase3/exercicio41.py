valor = int(input('Informe o valor da divida: '))

print('Valor Divida   Valor Juros   Parcelas    Valor da Parcela')
percent = 0.1

for i in range(0, 13, 3):
    if i == 0:
        juros = 0
        parcela = valor
        qtd = 1    
    else:
        juros = valor*percent
        percent += 0.05
        parcela = (valor+juros) / i
        qtd = i

    print('R$ {:.2f}\t{:.2f}\t{}\tR$ {:.2f}'.format(valor, juros, qtd, parcela))