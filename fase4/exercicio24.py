from random import randrange, randint
contador = [0,0,0,0,0,0]

for i in range(100):
    dado = randint(1,6)

    contador[dado-1] += 1

for i in range(len(contador)):
    print('{} - {} vezes'.format(i+1, contador[i])) 