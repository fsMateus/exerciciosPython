notas = []
cont = aux = 0

print('Digite -1 para encerrar a execução.')
while True:
    n = float(input('Digite a nota: '))
    if n == -1:
        break

    notas.append(n)

print('Quantidade: %d' % len(notas))
media = sum(notas)/len(notas)

msg = ''
for i in notas:
    msg += '%.2f ' % i
    if i > media:
        cont += 1
    if i < 7:
        aux += 1
print(msg)

notas.reverse()
for i in notas:
    print(i)

print('Soma: %.2f' % sum(notas))
print('Média: %.2f' % media)
print('Quantidade de notas acima da média:', cont)
print('Quantidade de notas abaixo de 7:', aux)

print('Encerrando...')