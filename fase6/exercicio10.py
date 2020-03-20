unidades = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
extras = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

num = int(input('digite o numero até 99: '))
if num > 0 and num < 10:
    print(unidades[num-1])
elif num < 20:
    print(extras[num-10])
elif num < 99:
    unidade = num % 10
    dezena = int(num/10)
    if unidade > 0:
        print('{} e {}'.format(dezenas[dezena-2], unidades[unidade-1]))
    else:
        print(dezenas[dezena-2])
