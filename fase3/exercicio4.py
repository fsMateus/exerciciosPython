a = 80000
b = 200000
tempo = 0

while a < b:
    a += a*0.03
    b += b*0.015
    tempo += 1

print('É necessário {} anos'.format(tempo)) 