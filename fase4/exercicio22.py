identificador = []
defeitos = [0,0,0,0]

print('Código de defeito:\n1- necessita da esfera\n2- necessita de limpeza\n3- necessita troca do cabo ou conector\n4- quebrado ou inutilizado')
print('Digite 0 na identificação para encerrar.')
while True:
    ident = int(input('Digite o número de identificação: '))

    if ident == 0:
        break
    
    defeito = int(input('Digite o código do defeito: '))
    if defeito >= 1 and defeito <= 4:
        identificador.append(ident)
        defeitos[defeito-1] += 1

print('Quantidade de mouses: {}'.format(len(identificador)))
print('Situação\tQuantidade\tPercentual')
for i in range(len(defeitos)):
    print('{}\t{}\t{:.2f}%'.format(i+1, defeitos[i], defeitos[i]/len(identificador)*100))