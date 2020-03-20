num = int(input('Informe o numero: '))
comeco = int(input('digite o valor de inicio: '))
fim = int(input('digite o valor de término: '))

print('Tabuada de {}:'.format(num))
if comeco < fim:
    for i in range(comeco, fim+1):
        print('{} x {} = {}'.format(num, i, num*i))
else:
    for i in range(fim, comeco+1):
        print('{} x {} = {}'.format(num, i, num*i))