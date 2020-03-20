salarios = []
abonos = []

while True:
    s = float(input('digite seu salário: '))
    if s == 0:
        break
    elif s < 0:
        print('valor inválido!')
    else:
        salarios.append(s)
        
print('\nSalário - Abono')
for i in salarios:
    abono = i*0.2 if i*0.2 > 100 else 100
    print('R$ {} - R$ {}'.format(i, abono))
    abonos.append(abono)

print('\nForam processados {} colaboradores'.format(len(salarios)))
print('Total gasto com abonos: R$ {}'.format(sum(abonos)))
print('Valor mínimo pago a {} colaboradores'.format(abonos.count(100)))
print('Maior valor de abono pago: R$ {}'.format(max(abonos)))