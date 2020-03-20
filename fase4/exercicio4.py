letras = ['b', 'd', 'e', 'p', 'a', 'x', 'v', 'w', 'i', 'k']
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = []
cont = 0

for i in letras:    
    if i.isalpha() and i not in vogais:
        cont += 1
        consoantes.append(i)

print('Existem {} consoantes. São elas {}'.format(cont, consoantes))