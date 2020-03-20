num = int(input('Digite seu código: '))
altura = int(input('Digite sua altura: '))
maior = menor = altura
alto = baixo = ''

for i in range(1, 10):
    num = int(input('Digite seu codigo: '))
    altura = int(input('Digite sua altura: '))

    info = 'número: {} - altura: {}'.format(num, altura)
    if altura > maior:
        alto = info
        maior = altura
    elif altura < menor:
        baixo = info
        menor = altura

print('Aluno mais alto = {}\nAluno mais baixo = {}'.format(alto, baixo))