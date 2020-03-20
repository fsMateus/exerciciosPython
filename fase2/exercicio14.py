nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 9:
    conceito = 'A'
    status = 'Aprovado'
elif media >= 7.5:
    conceito = 'B'
    status = 'Aprovado'
elif media >= 6:
    conceito = 'C'
    status = 'Aprovado'
elif media >= 4:
    conceito = 'D'
    status = 'Reprovado'
else:
    conceito = 'E'
    status = 'Reprovado'

print('Nota 1: {} Nota 2: {}\nMédia: {} Conceito: {}\nSituação: {}'.format(nota1, nota2, media, conceito, status))