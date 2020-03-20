salario = float(input('Informe seu salário atual: '))

if salario <= 280:
    percentual = '20%'
    aumento = salario*0.2
    novo_salario = salario + aumento
elif salario < 700:
    percentual = '15%'
    aumento = salario*0.15
    novo_salario = salario + aumento
elif salario < 1500:
    percentual = '10%'
    aumento = salario*0.1
    novo_salario = salario + aumento
else:
    percentual = '5%'
    aumento = salario*0.05
    novo_salario = salario + aumento

print('Salário: R$ {}\nPercentual de aumento aplicado: {}\nValor do aumento: R$ {}\nNovo Salário: R$ {}'.format(salario, percentual, aumento, novo_salario))