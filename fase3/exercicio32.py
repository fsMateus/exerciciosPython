n = int(input('digite o valor: '))
fat = n
msg = '{}! = {} '.format(n, n)

for i in range(1, n):
    fat *= (n-i)
    msg += '. %d '% (n-i)

print('Fatorial de %d: ' % n)
print(msg + '= %d' % fat)