nome = input("Digite seu nome: ")


while True:
    senha = input("Digite sua senha: ")
    if nome == senha:
        print("Senha invalida, digite novamente")
    else:
        break
