data = input('Digite a data no formato dd/mm/aaaa: ')

aux = data.split('/')

if int(aux[0]) <= 31 and int(aux[1]) <= 12 and len(aux[2]) == 4:
    print('É um data válida!')
else:
    print('Esta não é uma data válida')