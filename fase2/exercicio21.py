valor = int(input('Qual o valor você deseja sacar: '))

um = 0
cinco = 0
dez = 0
cinquenta = 0

if valor >= 10 and valor <= 600:
    unidade = valor % 10

    #obter dezena
    valor = (valor - unidade) / 10
    dezena = int(valor % 10)

    #obter centena    
    valor = (valor - dezena) / 10
    centena = int(valor)
    if centena >= 1:
        cem = '{} notas de cem'.format(centena)

    if dezena >= 5:
        cinquenta += 1
        dez = dezena - 5
        if dez >= 1:
            msg = '{} notas de cinquenta, {} notas de dez'. format(cinquenta, dez)
        else:
            msg = msg = '{} notas de cinquenta'.format(cinquenta)
    else:
        dez = dezena
        msg = '{} notas de dez'.format(dez)
    
    if unidade >= 5:
        cinco += 1
        um = unidade - 5
        if um >= 1:
            msg2 = '{} notas de cinco, {} notas de um'. format(cinco, um)
        else:
            msg2 = '{} notas de cinco'.format(cinco)
    else:
        um = unidade
        msg2 = '{} notas de um'.format(um)

    print('{}, {}, {}'.format(cem, msg, msg2))
else:
    print('Valor fora do limite estipulado.')