def converteHora(hora, minuto):
    if hora > 12:
        hora -= 12

    return hora, minuto

def ajustaSaida(h, m, turno):
    hora, minuto = converteHora(h, m)
    if turno.lower() == 'a':
        print('{}:{} A.M.'.format(hora, minuto))
    elif turno.lower() == 'p':
        print('{}:{} P.M.'.format(hora, minuto))
    else:
        print('turno inválido!')
        print('{}:{}'.format(hora, minuto))

print('digite hora igual -1 para encerrar a execução.')
while True:
    hora = int(input('Informe a hora: '))
    if hora == -1:
        break
    
    minuto = int(input('Informe os minutos: '))
    turno = input('Informe o turno: A-Até meio-dia P-Pós meio-dia ')

    ajustaSaida(hora, minuto, turno)