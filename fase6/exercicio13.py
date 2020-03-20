import random

with open('/home/avaliacao/Documentos/listaExercicios/fase6/arquivo.txt') as arquivo:
    linhas = arquivo.read().splitlines() #converte em lista
    arquivo.close()

palavra = random.choice(linhas)
aux = list(palavra)
embaralhada = ''.join(random.sample(palavra, len(aux)))

venceu = False
print('Que palavra é esta: {} ?'.format(embaralhada))
for i in range(6):
    resposta = input('digite sua resposta: ')
    if resposta.lower() == palavra.lower():
        print('{} -- {}\nGanhou!!'.format(resposta, palavra))
        venceu = True
        break

if not venceu:
    print('Perdeu')