# encoding:utf-8

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

def criaRelatorio(num, nomes, consumosMega, percentuais):
    if (len(nomes) == len(consumosMega) == len(percentuais)):        
        codigo_html = '<html>\n<head>\n<title>Relatorio</title>\n</head>\n<body>\n<h1>Relatorio Armazenamento</h1>\n'
        codigo_html += '<table style="width:80%">\n<tr>\n<th>Ordem</th>\n<th>Nome</th>\n<th>Consumo</th>\n<th>Porcentagem</th>\n</tr>\n'
        ordenado = sorted(percentuais, reverse=True)
        open('index.html','a')
        arquivo = open('index.html','w')
        arquivo.write(codigo_html)
        if num <= len(nomes):
            for i in range(num):
                pos = percentuais.index(ordenado[i])
                arquivo.write('<tr>\n'+'<td>'+str(i+1)+'</td>\n'+'<td>'+str(nomes[pos])+'</td>\n'+'<td>'+str(consumosMega[pos])+' MB</td>\n'+'<td>'+str(percentuais[pos])+'%</td>\n'+'</tr>\n')
        else:
            for i in range(len(nomes)):
                pos = percentuais.index(ordenado[i])
                arquivo.write('<tr>\n'+'<td>'+str(i+1)+'</td>\n'+'<td>'+str(nomes[pos])+'</td>\n'+'<td>'+str(consumosMega[pos])+' MB</td>\n'+'<td>'+str(percentuais[pos])+'%</td>\n'+'</tr>\n')
        
        arquivo.write('</table>\n')
        totalConsumo = sum(consumosMega)
        consumoMedio = espacoMedio(consumosMega)
        arquivo.write('<p>Consumo Total: '+str(totalConsumo)+' MB</p>\n'+'<p>Consumo Medio: '+str(consumoMedio)+'</p>\n')
        arquivo.write('</body>\n</html>')
        arquivo.close()
    else:
       print('Quantidade de Usuarios e Dados Não Conferem.')


num = int(input('digite a quantidade desejada: '))
nomes = ajustaNomes(linhas)
consumos = tamanhoConsumido(linhas)
consumosMega = transformaMB(consumos)
percentuais = calculaPercentuais(consumosMega)
criaRelatorio(num, nomes,consumosMega,percentuais)


# with open('/home/avaliacao/Documentos/listaExercicios/relatorio.txt') as relatorio:
#     for linha in relatorio:
#         print(linha)
#     relatorio.close()