while True:
    notas = []
    nome = input('Informe o nome do atleta: ')
    if nome == '':
        break

    for i in range(7):
        notas.append(float(input('Nota: ')))

    melhor = max(notas)
    notas.remove(melhor)
    pior = min(notas)
    notas.remove(pior)
    media = sum(notas)/len(notas)
    print('\nResultado Final:\nAtleta: {}\nMelhor nota: {}\nPior nota: {}\nMédia: {:.2f}\n'.format(nome, melhor, pior, media))