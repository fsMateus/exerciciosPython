parcelas = []

def valorPagamento(valor, dias):
    if dias > 0:
        juros = 0
        multa = valor*0.03
        for i in range(dias):
            juros += valor*0.1

        valor += multa + juros
    
    parcelas.append(valor)
    return valor

print('Digite 0 no valor da parcela, para encerrar.')
while True:
    valor = float(input('Digite o valor da parcela: '))
    if valor == 0:
        break

    atraso = int(input('Informe a quantidade de dias de atraso: '))

    valorPagamento(valor, atraso)

print('Quantidade de parcelas pagas hoje: {} - Total recebido: R$ {:.2f}'.format(len(parcelas), sum(parcelas)))