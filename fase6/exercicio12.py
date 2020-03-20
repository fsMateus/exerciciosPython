fone = input('digite o numero de telefone: ')
num = fone.replace('-','')

print('Telefone: {}'.format(fone))
if len(num) == 7:    
    corrigido = '3' + num
    formatado = '{}-{}'.format(corrigido[:4], corrigido[4:])
    print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
    print('Telefone corrigido sem formatação: {}'.format(corrigido))
    print('Telefone corrigido com formatação: {}'.format(formatado))
else:
    formatado = '{}-{}'.format(num[:4], num[4:])
    print('Telefone com formatação: {}'.format(formatado))