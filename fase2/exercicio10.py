letra = input('Em que turno você estuda?\nM - Matutino\nV - Vespertino\nN - Noturno\n')

letra = letra.lower()
if letra == 'm':
    print('Bom dia!')
elif letra == 'v':
    print('Boa tarde!')
elif letra == 'n':
    print('Boa noite!')
else:
    print('Valor Inválido!')