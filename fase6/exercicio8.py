palavra = input('Digite o texto: ')

semEspaco = palavra.replace(' ','')
invertida = palavra.lower()[::-1]

if palavra.lower() == invertida:
    print('{} -- {}\né palindromo'.format(palavra, invertida))
else:
    print('{} -- {}\n não é palindromo'.format(palavra, invertida))