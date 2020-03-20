opcao = 's'
while opcao == 's':
    a = float(input('Digite o tamanho da população A: '))
    taxa_a = float(input('Digite a taxa anual de crescimento da população A: '))
    b = float(input('Digite o tamanho da população B: '))
    taxa_b = float(input('Digite a taxa anual de crescimento da população B: '))    
    tempo = 0

    if a > 0 and b > 0 and taxa_a > 0 and taxa_b > 0:
        while a < b:
            a += a*taxa_a
            b += b*taxa_b
            tempo += 1

        print('É necessário {} anos'.format(tempo))
        opcao = input('Desejar repetir a operação: S-Sim N-Não ')

    else:
        print('Todas as entradas devem ser maior que 0. ')
        opcao = input('Desejar repetir a operação: S-Sim N-Não ')
