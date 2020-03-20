frase = input('digite a frase: ')
espacos = frase.count(' ')
vogais = ['a', 'e', 'i', 'o', 'u']
cont = 0

for i in frase:
    if i in vogais:
        cont += 1

print('Existe {} espaços, e {} vogais'.format(espacos, cont))