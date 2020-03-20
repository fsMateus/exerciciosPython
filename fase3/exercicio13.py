while True:
    base = float(input('Digite o numero base: '))
    expoente = float(input('Digite o numero expoente: '))

    print(base**expoente)
    
    opcao = input('Deseja repetir operação: S-Sim N-Não ')
    
    if opcao.lower() == 'n':
        break