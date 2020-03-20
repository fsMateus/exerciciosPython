maior = soma = cont = 0
menor = 10
gabarito = ['a', 'b', 'c', 'd', 'e', 'e', 'd', 'c', 'b', 'a']
notas = []

while True:
    acertos = 0
    for i in range(10):
        resposta = input('Digite sua resposta para questão {}: '.format(i+1))
  
        if resposta.lower() == gabarito[i]:
            acertos += 1

    if acertos > maior:
        maior = acertos
    if acertos < menor:
        menor = acertos
    
    cont += 1
    soma += acertos

    opcao = input('Outro aluno vai usar o sistema - S-Sim N-Não: ')
    if opcao.lower() == 'n':
        break

print('Maior: {} - Menor: {}\nTotal de alunos: {}\nMédia da Turma: {:.2f}'.format(maior, menor, cont, soma/cont))