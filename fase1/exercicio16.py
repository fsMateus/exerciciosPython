area = float(input('informe o tamanho da área a ser pintada, em m²: '))
qtd_latas = round(area / (18*3))

print('É necessário comprar {} latas de tinta, o valor total é R$: {}'.format(qtd_latas, qtd_latas*80))