# nota1, nota2, nota3, nota4 = input("Digite 4 valores separados por espaço: ").split()

vet = []
soma = 0

for i in range(4):
    numero = float(input(f"Digite a nota {i + 1}: "))
    vet.append(numero)

for i in range(4):
    print(f"Nota {i+1}: {vet[i]} ")

for i in range(4):
    soma = soma + vet[i]

print("A média é:", soma/4)