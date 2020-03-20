qtd_litros = int(input('Digite a quantidade de litros desejado: '))
tipo = input('Informe o tipo de combustível - A-Alcool G-Gasolina: ')

if tipo.lower() == 'a':
    if qtd_litros > 20:
        preco = 1.90*qtd_litros
        preco = preco - preco*0.05
    else:
        preco = 1.90*qtd_litros
        preco = preco - preco*0.03
elif tipo.lower() == 'g':
    if qtd_litros > 20:
        preco = 1.90*qtd_litros
        preco = preco - preco*0.06
    else:
        preco = 1.90*qtd_litros
        preco = preco - preco*0.04

print('O valor total é R$ {}'.format(preco))