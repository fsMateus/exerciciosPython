tamanho = float(input('informe o tamanho do arquivo: '))
velocidade = float(input('informe a velocidade da internet: '))

tempo = tamanho / velocidade

print('O tempo aproximado para download é de {} minutos'.format(tempo/60))