while True:
    num = float(input('Digite uma nota entre 0 e 10 '))
    if num < 0 or num > 10:
        print('Valor digitado é inválido!')
        break