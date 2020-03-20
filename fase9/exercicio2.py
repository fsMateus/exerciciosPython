strings=[]
arquivo=open("logsApache.txt", "r")
site="www.tins.com"
listaPalavras = []

for linha in arquivo:
    strings.append(linha.split())

for www in strings:
    if www[1]==site:
        if listaPalavras.count(www[0])==0:
            listaPalavras.append(www[0])

print("Palavras pesquisadas que ajudam a chegar no site", site)
for i in listaPalavras:
    print(i)
