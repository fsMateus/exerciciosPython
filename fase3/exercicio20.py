while True:
    n = int(input('digite um número (entre 0 e 16): '))
    if n > 0 and n < 16:
        fat = n

        for i in range(1, n):
            fat *= (n-i)

        print('Fatorial de {} é {}'.format(n, fat))
        opcao = input('Deseja repetir operação S-Sim N-Não: ')

        if opcao.lower() == 'n':
            break
    else:
        print('Valor Inválido! O valor deve está entre 0 e 16.')
        opcao = input('Deseja repetir operação S-Sim N-Não: ')

        if opcao.lower() == 'n':
            break