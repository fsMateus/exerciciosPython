while True:
    nome = input('Digite seu nome: ')
    senha = input('Digite a senha: ')

    if senha.lower() == nome.lower():
        print('A senha deve ser diferente do nome. Informe os dados novamente')
    else:
        print('Login realizado com sucesso!')
        break