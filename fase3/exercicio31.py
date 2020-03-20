print('Digite 0 para concluir')
precos = []
soma = 0

while True:
    preco = float(input('digite o preço do produto: '))
    precos.append(preco)
    soma += preco

    if preco == 0:
        for i in range(len(precos)):
            print('Produto {}: R$ {:.2f}'.format(i+1, precos[i]))
        
        print('Total: R$ %.2f' % soma)
        dinheiro = float(input('Informe o valor em dinheiro: '))
        if dinheiro < soma:
            print('Valor abaixo do total')
            break
        else:
            troco = dinheiro - soma
            print('Dinheiro: R$ {:.2f}\nTroco: R$ {:.2f}\n...'.format(dinheiro, troco))
            precos = []
            soma = 0