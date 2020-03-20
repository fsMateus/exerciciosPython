dados = [{'codigo': 1, 'veiculos': 7000,'acidentes': 40},
    {'codigo': 2, 'veiculos': 10000, 'acidentes': 47},
    {'codigo': 3, 'veiculos': 1000, 'acidentes': 20},
    {'codigo': 4, 'veiculos': 900, 'acidentes': 13},
    {'codigo': 5, 'veiculos': 4000, 'acidentes': 35}]

maior = menor = dados[0]['acidentes']
mais = menos = ''
soma = 0
poucos = 0
cont = 0

for i in range(5):
    soma += dados[i]['veiculos']
    
    msg = 'Indice de acidentes: {} - Cidade: {}'.format(dados[i]['acidentes'], dados[i]['codigo'])
    if dados[i]['acidentes'] > maior:
        mais = msg
        maior = dados[i]['acidentes']
    elif dados[i]['acidentes'] < menor:
        menos = msg
        menor = dados[i]['acidentes']

    if dados[i]['veiculos'] < 2000:
        poucos += dados[i]['acidentes']
        cont += 1

print('{} {}\nMédia de veiculos: {}\nMédia de acidentes: {}'.format(mais, menos, soma/5, poucos/cont))