print('Digite um valor negativo para encerrar a execução.')
item1 = item2 = item3 = item4 = item5 = item6 = 0
while True:
    cod = int(input('Digite o código do produto: '))
    if cod < 0:
        break
    
    qtd = int(input('Digite a quantidade: '))

    if cod == 100:
        item1 += qtd*1.20        
    elif cod == 101:
        item2 += qtd*1.30        
    elif cod == 102:
        item3 += qtd*1.50
    elif cod == 103:
        item4 += qtd*1.20        
    elif cod == 104:
        item5 += qtd*1.30        
    elif cod == 105:
        item6 += qtd*1

total = item1 + item2 + item3 + item4 + item5 + item6
print('Código - 100: {:.2f}\nCódigo - 101: {:.2f}\nCódigo - 102: {:.2f}\nCódigo - 103: {:.2f}\nCódigo - 104: {:.2f}\nCódigo - 105: {:.2f}\nTotal: {:.2f}'.format(item1, item2, item3, item4, item5, item6, total))