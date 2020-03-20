while True:
    saltos = []
    msg = ''
    nome = input('Informe o nome do atleta: ')
    if nome == '':
        break

    for i in range(5):
        v = float(input('digite a distancia do salto {}: '.format(i+1)))
        saltos.append(v)

        if i == 0:
            msg += '%.1f' % v
        else:
            msg += ' - %.1f' % v
        
    
    media = sum(saltos)/len(saltos)
    print('\nResultado Final:\nAtleta: {}\nSaltos: {}\nMédia dos saltos: {:.2f}m\n'.format(nome, msg, media))