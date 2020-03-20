import datetime

def valiData(data):
    dia, mes, ano = data.split('/')    
    valido = True
    try:
        datetime.datetime(int(ano), int(mes), int(dia))
    except:
        valido = False

    return valido

def dataExtenso(data):    
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    if valiData(data):
        dia, mes, ano = data.split('/')
        print('{} de {} de {}'.format(dia, meses[int(mes)-1], ano))
    else:
        print('Data no formato inválido')


data = input('informe uma data no formato (DD/MM/AAAA): ')
dataExtenso(data)