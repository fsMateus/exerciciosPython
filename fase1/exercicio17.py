area = float(input('informe o tamanho da área a ser pintada, em m²: '))

qtd_latas18 = round(area / (18*6))
qtd_latas3 = round(area / (3.6*6))

litros = area/6 + (area/6)*0.1
latas = 0
galoes = 0

while True:
    if litros > 11:
        latas += 1
        litros -= 18
    else:
        galoes += 1
        litros -= 3.6
    
    if litros <= 0:
        break
     

print('Apenas latas: \nÉ necessário comprar {} latas de tinta, o valor total é R$: {}\n'.format(qtd_latas18, qtd_latas18*80))
print('Apenas Galões: \nÉ necessário comprar {} galões de tinta, o valor total é R$: {}\n'.format(qtd_latas3, qtd_latas3*25))
print('Misturados: \nÉ necessário comprar {} latas de tinta, e {} galões de tinta, o valor total é R$: {}\n'.format(latas, galoes, latas*80 + galoes*25))