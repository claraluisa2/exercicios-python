vet = []

for i in range(10):
    caractere = input("Digite um caratere: ").lower() # deixa tudo em minuscula
    vet.append(caractere)

vogais = {'a', 'e', 'i', 'o', 'u'}

consoantes = [c for c in vet if c.isalpha() and c not in vogais]

print(f"Foram lidas {len(consoantes)} consoantes.")
print("As consoantes são:", consoantes)