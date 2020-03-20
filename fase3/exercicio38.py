import datetime
ano_atual = datetime.datetime.now().year

tempo = ano_atual - 1995
salario = 1000
percentual = 0.015

for i in range(tempo):
    print(percentual)
    salario = salario + salario*percentual
    percentual = percentual * 2
    
print('O salário atual é R$ {:.2f}'.format(salario))