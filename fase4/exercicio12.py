dados = [{'idade': 18, 'altura': 1.66}, {'idade': 23, 'altura': 1.76}, {'idade': 14, 'altura': 1.58},
    {'idade': 17, 'altura': 1.68}, {'idade': 11, 'altura': 1.53}, {'idade': 13, 'altura': 1.55},
    {'idade': 27, 'altura': 1.72}, {'idade': 22, 'altura': 1.68}, {'idade': 21, 'altura': 1.70},
    {'idade': 16, 'altura': 1.70}, {'idade': 25, 'altura': 1.60}, {'idade': 28, 'altura': 1.72},
    {'idade': 29, 'altura': 1.77}, {'idade': 24, 'altura': 1.62}, {'idade': 14, 'altura': 1.61},
    {'idade': 12, 'altura': 1.50}, {'idade': 11, 'altura': 1.47}, {'idade': 19, 'altura': 1.68},
    {'idade': 13, 'altura': 1.49}, {'idade': 12, 'altura': 1.56}, {'idade': 28, 'altura': 1.70},
    {'idade': 15, 'altura': 1.62}, {'idade': 16, 'altura': 1.69}, {'idade': 19, 'altura': 1.73},
    {'idade': 20, 'altura': 1.68}, {'idade': 26, 'altura': 1.78}, {'idade': 15, 'altura': 1.60},
    {'idade': 29, 'altura': 1.68}, {'idade': 27, 'altura': 1.79}, {'idade': 18, 'altura': 1.64}]

cont = 0
soma = 0
for i in dados:
    soma += i['altura']

media = soma / len(dados)
for i in dados:
    if i['idade'] > 13 and i['altura'] < media:
        cont += 1

print(cont)