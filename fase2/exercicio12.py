valor_hora = float(input('Informe o valor da hora de trabalho: '))
qtd_horas = float(input('Informe a quantidade de horas trabalhadas: '))

salario_bruto = valor_hora*qtd_horas

if salario_bruto <= 900:
    ir = '0%'
    valor_ir = salario_bruto*0
    inss = salario_bruto*0.1
    sindicato = salario_bruto*0.03
    fgts = salario_bruto*0.11
    descontos = valor_ir + inss + sindicato
    salario = salario_bruto - descontos
elif salario_bruto <= 1500:
    ir = '5%'
    valor_ir = salario_bruto*0.05
    inss = salario_bruto*0.1
    sindicato = salario_bruto*0.03
    fgts = salario_bruto*0.11
    descontos = valor_ir + inss + sindicato
    salario = salario_bruto - descontos
elif salario_bruto <= 2500:
    ir = '10%'
    valor_ir = salario_bruto*0.1
    inss = salario_bruto*0.1
    sindicato = salario_bruto*0.03
    fgts = salario_bruto*0.11
    descontos = valor_ir + inss + sindicato
    salario = salario_bruto - descontos
else:
    ir = '20%'
    valor_ir = salario_bruto*0.2
    inss = salario_bruto*0.1
    sindicato = salario_bruto*0.03
    fgts = salario_bruto*0.11
    descontos = valor_ir + inss + sindicato
    salario = salario_bruto - descontos

print('Salário Bruto: R$ {}\n(-) IR ({}): R$ {}\n(-)INSS (10%): R$ {}\n(-)Sindicato (3%): R$ {}\nFGTS (11%): R$ {}\nTotal de descontos: R$ {}\nSalário Liquido: R$ {}'.format(salario_bruto, ir, valor_ir, inss, sindicato, fgts, descontos, salario))