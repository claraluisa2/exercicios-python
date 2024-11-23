vetor = []

# Lê 10 números reais do usuário
for i in range(10):
    numero = float(input(f"Digite o número {i + 1}: "))
    vetor.append(numero)

# Mostra os números na ordem inversa
print("Os números na ordem inversa são:")
for numero in reversed(vetor):
    print(numero)



#depos faça de maneira recursiva como em programação funcional!!