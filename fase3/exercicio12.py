num = int(input('Informe o numero: '))

print('Tabuada de {}:'.format(num))
for i in range(1, 11):
    print('{} x {} = {}'.format(num, i, num*i))