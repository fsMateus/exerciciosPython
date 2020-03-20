def valor(valor):
    if valor == '':
        return int(1)
    else:
        return faixa_valida(int(valor))

def faixa_valida(valor):
    if valor<1:
        return 1
    elif valor>20:
        return 20
    else:
        return valor

def criaLinha(linha):
    l='+'
    for x in range(linha):
        l+='-'
    l+='+'
    print(l)

def criaColuna(linha, coluna):
    for y in range(coluna):
        c='|'
        c+= ' '*linha
        c+='|'
        print(c)

def desenhaMoldura(linha, coluna):
    criaLinha(linha)
    criaColuna(linha, coluna)
    criaLinha(linha)

linha = input('Diga quantos +----+, entre 1 e 20: ')
coluna = input('Diga quantos |    |, entre 1 e 20: ')
desenhaMoldura(valor(linha), valor(coluna))