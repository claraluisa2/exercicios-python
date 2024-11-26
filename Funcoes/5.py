def somaImposto(taxaImposto, custo):
    custo = custo+taxaImposto
    return custo

custo = 56

custo = somaImposto(3,custo)

print(custo)