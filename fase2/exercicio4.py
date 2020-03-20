letra = input('digite uma letra: ')
letra = letra.lower()

vogais = ['a', 'e', 'i', 'o', 'u']

if letra.isdigit():
    print('O valor {} é um digito'.format(letra))
elif letra in vogais:
    print('A letra {} é uma vogal'.format(letra))
else:
    print('A letra {} é uma consoante'.format(letra))