vet = [0,1,2,3,4,5]

print(vet)

for i in range(len(vet)):
    print(vet[i])

vetor = list(map(int, input("Digite os elementos do vetor separados por espaço: ").split()))

print(vetor)

for i in range(len(vetor)):
    print(vetor[i])


# map: transforma cada elemento de um iterável aplicando uma função.
# list: converte um iterável (como o resultado de map) em uma lista.