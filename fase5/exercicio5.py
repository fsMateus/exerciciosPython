def somaImposto(taxa, custo):
    custo += custo*taxa 
    return custo

valor = float(input('digite o valor do produto: '))
imposto = float(input('informe a taxa de imposto: '))

print('Valor com imposto: {:.2f}'.format(somaImposto(imposto, valor)))