preco_pao = float(input('Digite o preço do pão: '))
print('Preço do pão: R$ %f' % preco_pao)
print('Panificadora Pão de Ontem - Tabela de preços')
for i in range(50):
    print('{} - R$ {:.2f}'.format(i+1, (i+1)*preco_pao))