numeros = []
for i in range(5):
    numeros.append(int(input('Digite um numero: ')))

maior = numeros[0]
for i in numeros:
    maior = i if i > maior else maior

print(maior)
print(max(numeros))