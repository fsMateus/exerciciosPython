pares = []
impares = []

for i in range(10):
    num = int(input('Digite o numero: '))

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('A quantidade de valores pares é {} são eles {}, e a quantidade de impares é {} são eles{}'.format(len(pares), pares, len(impares), impares))

# qtd_par = 0
# qtd_impar = 0

# for i in range(10):
#     num = int(input('Digite o numero: '))

#     if num % 2 == 0:
#         qtd_par += 1
#     else:
#         qtd_impar += 1

# print('A quantidade de valores pares é {}, e a quantidade de impares é {}'.format(qtd_par, qtd_impar))