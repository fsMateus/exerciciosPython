meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas = []
for i in range(12):
    temperaturas.append(float(input('digite a temperatura: ')))

media = sum(temperaturas)/len(temperaturas)
print('\nTemperatura média anual: %.2f\n' % media)
for i in range(12):
    if temperaturas[i] > media:
        print('Mês: {} - Temperatura: {}'.format(meses[i], temperaturas[i]))