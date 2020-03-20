valor_hora = float(input('informe o valor da hora de trabalho '))
qtd_horas = float(input('informe a quantidade de horas trabalhadas '))

salario_bruto = valor_hora*qtd_horas
ir = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print('+ Salário Bruto: R$ {} \n- IR (11%): R$ {} \n -INSS (8%): R$ {} \n -Sindicato (5%): R$ {} \n= Salário Liquido: R$ {} \n'.format(salario_bruto, ir, inss, sindicato, salario_liquido))