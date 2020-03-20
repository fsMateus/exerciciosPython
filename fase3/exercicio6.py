for i in range(20):
    print(i+1)

print('\n')
msg = ''
for i in range(20):
    msg += '{}'.format(i+1)
    if i+1 < 20:
        msg += ', '

print(msg)