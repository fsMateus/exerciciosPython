num = int(input('Digite um numero inteiro menor que 1000: '))
origin = num

if num < 1000:
    #obter unidade
    unidade = num % 10

    #obter dezena
    num = (num - unidade) / 10
    dezena = num % 10

    #obter centena    
    num = (num - dezena) / 10
    centena = num

    print('{} = {} centena(s), {} dezena(s) e {} unidade(s)'.format(origin, int(centena), int(dezena), unidade))
else:
    print('Valor inválido')