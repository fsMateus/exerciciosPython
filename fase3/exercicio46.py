while True:
    saltos = []
    nome = input('Informe o nome do atleta: ')
    if nome == '':
        break

    for i in range(5):
        saltos.append(float(input('digite a distancia do salto {}: '.format(i+1))))

    melhor = max(saltos)
    saltos.remove(melhor)
    pior = min(saltos)
    saltos.remove(pior)
    media = sum(saltos)/len(saltos)
    print('Melhor salto: {}m\nPior salto: {}m\nMédia dos demais saltos: {:.2f}m\n\nResultado Final:\n{}: {:.2f}m'.format(melhor, pior, media, nome, media))