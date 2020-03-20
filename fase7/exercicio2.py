with open('/home/avaliacao/Documentos/listaExercicios/fase7/usuarios.txt') as arquivo:
    linhas = arquivo.read().splitlines() #converte em lista
    arquivo.close()

def ajustaNomes(lista):
    listaNome = []
    for i in range(len(lista)):
       listaNome.append(lista[i][0:14].rstrip())
    return listaNome

def tamanhoConsumido(lista):
    listaConsumo = []
    for i in range(len(lista)):
        listaConsumo.append(int(lista[i][15:len(lista[i])]))
    return listaConsumo

def transformaMB(lista):
    listaEmMega = []
    for i in range(len(lista)):
        listaEmMega.append(round(int(lista[i])/(1024*1024)))
    return listaEmMega

def calculaPercentuais(lista):
    percentuais = []
    valorTotal = sum(lista)
    for i in range(len(lista)):
       percentuais.append(round((lista[i]/valorTotal)*100,2))
    return percentuais

def espacoMedio(lista):
    espacoMedio = round(sum(lista)/len(lista),2)
    return espacoMedio

def criaRelatorio(nomes, consumosMega, percentuais):
    if (len(nomes) == len(consumosMega) == len(percentuais)):
        open('relatorio.txt','a')
        arquivo = open('relatorio.txt','w')
        for i in range(len(nomes)):
            arquivo.write(str(i+1)+' '+str(nomes[i])+' '+str(consumosMega[i])+'MB '+str(percentuais[i])+'%'+'\n')
        totalConsumo = sum(consumosMega)
        consumoMedio = espacoMedio(consumosMega)
        arquivo.write('Consumo Total: '+str(totalConsumo)+'\n'+'Consumo Medio: '+str(consumoMedio)+'\n')
        arquivo.close()
    else:
       print('Quantidade de Usuarios e Dados Não Conferem.')

nomes = ajustaNomes(linhas)
consumos = tamanhoConsumido(linhas)
consumosMega = transformaMB(consumos)
percentuais = calculaPercentuais(consumosMega)
criaRelatorio(nomes,consumosMega,percentuais)

with open('/home/avaliacao/Documentos/listaExercicios/relatorio.txt') as relatorio:
    for linha in relatorio:
        print(linha)
    relatorio.close()