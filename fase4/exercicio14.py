respostas = []

print('Responda as perguntas abaixo com S-Sim ou N-Não')
respostas.append(input('Telefonou para vitima? '))
respostas.append(input('Esteve no local do crime? '))
respostas.append(input('Mora perto da vítima? '))
respostas.append(input('Devia para a vítima? '))
respostas.append(input('Já trabalhou com a vítima? '))

if respostas.count('s') == 5:
    print('Assassino')
elif respostas.count('s') == 2:
    print('Suspeito')
elif respostas.count('s') > 2 and respostas.count('s') < 5:
    print('Cúmplice')
else:
    print('Inocente')