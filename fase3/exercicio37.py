maior = ''
menor = ''
mais_gordo = ''
mais_magro = ''

codigo = int(input('digite seu codigo: '))
altura = float(input('digite sua altura em metros: '))
peso = float(input('digite seu peso: '))

alto = baixo = altura
gordo = magro = peso

soma_altura = 0
soma_peso = 0
qtd = 0

while True:
    codigo = int(input('digite seu codigo: '))
    if codigo == 0:
        break

    altura = float(input('digite sua altura em metros: '))
    peso = float(input('digite seu peso: '))

    info = 'codigo: {}, altura: {}, peso: {}'.format(codigo, altura, peso)
    soma_altura += altura
    soma_peso += peso
    qtd += 1

    if altura > alto:
        maior = info
        alto = altura
    elif altura < baixo:
        menor = info
        baixo = altura

    if peso > gordo:
        mais_gordo = info
        gordo = peso
    elif peso < magro:
        mais_magro = info
        magro = peso

print('Cliente mais alto = {}\nCliente mais baixo = {}\nCliente mais gordo = {}\nCliente mais magro = {}\nMédia de altura: {} - Média de peso'.format(maior, menor, mais_gordo, mais_magro, soma_altura/qtd, soma_peso/qtd))