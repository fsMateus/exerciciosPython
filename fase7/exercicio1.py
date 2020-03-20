import re 
 
regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

def check(Ip): 
	
	if(re.search(regex, Ip)): 
		return True		
	else: 
		return False

with open('/home/avaliacao/Documentos/listaExercicios/fase7/ips.txt') as arquivo:
    linhas = arquivo.read().splitlines() #converte em lista
    arquivo.close()

def criaRelatorio(ips):
    open('ip_valido.txt','a')
    validos = open('ip_valido.txt','w')

    open('ip_invalido.txt','a')
    invalidos = open('ip_invalido.txt','w')

    for i in range(len(ips)):
        if check(ips[i]):                       
            validos.write(str(ips[i])+'\n')            
        else:            
            invalidos.write(str(ips[i])+'\n')
        
    validos.close()
    invalidos.close()

    open('lista_ip.txt','a')
    arq = open('lista_ip.txt','w')
    
    lista1 = open('ip_valido.txt','r')
    conteudo1 = lista1.readlines()
    lista2 = open('ip_invalido.txt','r')
    conteudo2 = lista2.readlines()

    arq.write('[Endereços Válidos]\n')
    arq.writelines(conteudo1)
    arq.write('\n[Endereços Inválidos]\n')
    arq.writelines(conteudo2)

    arq.close()

ips = linhas
criaRelatorio(ips)