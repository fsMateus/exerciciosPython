n = int(input('digite o valor: '))
fat = n

for i in range(1, n):
    fat *= (n-i)

print('Fatorial de {} é {}'.format(n, fat))

# origin = n
# while n > 1:
#     fat *= n-1
#     n -= 1

# print('Fatorial de {} é {}'.format(origin, fat))