kg_maca = float(input('informe a quantidade de quilos de maçã: '))
kg_morango = float(input('informe a quantidade de quilos de morango: '))

if kg_maca <= 5:
    preco_maca = 2.50*kg_maca
else:
    preco_maca = 2.20*kg_maca

if kg_morango <= 5:
    preco_morango = 1.80*kg_morango
else:
    preco_morango = 1.50*kg_morango

preco = preco_maca + preco_morango

if kg_maca + kg_morango > 8 or preco > 25:
    preco = preco - preco*0.1

print('O valor total a ser pago é R$ {}'.format(preco))