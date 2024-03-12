from funcoes import login

while True:
    user = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
    if login(user,senha):
        break
    else:
        print('Tente novamente!')

