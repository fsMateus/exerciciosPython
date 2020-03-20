carros = ['Fusca', 'Gol', 'Onix', 'Corolla', 'Sandero']
consumo = [7, 10, 12.5, 9, 14.5]

# for i in range(5):
#     print('Veiculo {}\nNome: {}\nKm por litro: {}'.format(i+1, carros[i], consumo[i]))

print('Relatório Final: ')
for i in range(5):
    print('{} - {} - {} - {:.2f} litros - R$ {:.2f}'.format(i+1, carros[i], consumo[i], 1000/consumo[i], 1000/consumo[i]*2.25))

pos = consumo.index(max(consumo))
print('O menor consumo é do {}'.format(carros[pos]))