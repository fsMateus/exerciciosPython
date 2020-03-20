salarios = []
contadores = [0,0,0,0,0,0,0,0,0]
print('Digite -1 para encerrar a execução.')
while True:
    valor = float(input('Informe o valor de vendas da semana: '))
    if valor == -1:
        break
    
    s = 200 + valor*0.09
    salarios.append(s)

for i in salarios:
    pos = int(i/100 - 2)
    contadores[pos] += 1

for i in range(len(contadores)):
    if contadores[i] > 0:
        print('{} - entre[{}00-{}99]'.format(contadores[i], i+2, i+2))