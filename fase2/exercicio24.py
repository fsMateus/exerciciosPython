num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

operador = input('Indique a operação a ser realizada: + - * / ')
if operador == '+':
    resultado = num1 + num2    
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    resultado = num1 / num2
else:
    print('Operador inválido!')


if resultado % 2 == 0:
    msg = '{}, é um valor par'.format(resultado)
else:
    msg = '{}, é um valor impar'.format(resultado)

if resultado == round(resultado):
    msg2 = ('inteiro')
else:
    msg2 = ('decimal')

if resultado > 0:
    msg3 = ('positivo')
else:
    msg3 = ('negativo')

print('{}, {}, {}'.format(msg, msg2, msg3))