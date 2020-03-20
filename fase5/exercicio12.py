import random

def embaralha(termo):
    aux = list(termo)
    t = ''.join(random.sample(termo, len(aux)))
    
    print(t.lower())

p = input('digite uma palavra: ')
embaralha(p)