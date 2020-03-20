while True:
    nome = input('Digite seu nome')

    if len(nome) <= 3:
        print('Nome deve possuir mais que 3 caracteres.')
    else:
        break

while True:
    idade = int(input('Digite sua idade: '))

    if idade < 0 or idade > 150:
        print('Idade deve está no limite de 0 a 150 ')
    else:
        break

while True:
    salario = float(input('Digite seu salário'))

    if salario <= 0:
        print('O valor do salário deve ser maior que 0. ')
    else:
        break

while True:
    sexo = input('Informe o seu sexo F-Feminino M-Masculino: ')

    if sexo.lower() == 'f' or sexo.lower() == 'm':
        break
    else:
        print('Valor inválido, informe novamente - F ou M ')

while True:
    estado = input('Informe seu estado civil: S-Solteiro C-Casado V-Viúvo D-Divorciado ')

    if estado.lower() == 's' or estado.lower() == 'c' or estado.lower() == 'v' or estado.lower() == 'd':
        break
    else:
        print('Valor inválido, informe novamente - S C V D ')