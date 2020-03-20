def leet(texto):
    getchar = lambda c: letras[c] if c in letras else c
    letras = {"a":"4","e":"3","l":"1","o":"0","s":"5"}
    return ''.join(getchar(c) for c in texto)

texto = input('Digite a frase: ')
print(leet(texto))