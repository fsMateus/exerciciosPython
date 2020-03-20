tipo_carne = input('Qual tipo de carne: F-File Duplo A-Alcatra P-Picanha ')
qtd_kilos = float(input('Qual a quantidade comprada: '))
pagamento = input('Qual o tipo de pagamento: D-Dinheiro C-Cartão: ')

if tipo_carne.lower() == 'f':
    nome = 'File Duplo'
    if qtd_kilos <= 5:
        preco = 4.90*qtd_kilos
    else:
        preco = 5.80*qtd_kilos
elif tipo_carne.lower() == 'a':
    nome = 'Alcatra'
    if qtd_kilos <= 5:
        preco = 5.90*qtd_kilos
    else:
        preco = 6.80*qtd_kilos
elif tipo_carne.lower() == 'p':
    nome = 'Picanha'
    if qtd_kilos <= 5:
        preco = 6.90*qtd_kilos
    else:
        preco = 7.80*qtd_kilos
else:
    nome = ''
    print('Inválido!')

if pagamento.lower() == 'c':
    tipo_pag = 'Cartão'
    desconto = preco*0.05
    novo_preco = preco - desconto
else:
    tipo_pag = 'Dinheiro'
    desconto = 0
    novo_preco = preco


print('Tipo de Carne: {}, Quantidade: KG {}\nPreço Total: R$ {}\nTipo de Pagamento: {}\nValor do Desconto: R$ {:.2f} - Valor a Pagar: R$ {:.2f}'.format(nome, qtd_kilos, preco, tipo_pag, desconto, novo_preco))