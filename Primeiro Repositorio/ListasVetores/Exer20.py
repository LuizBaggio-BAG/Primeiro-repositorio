def permutacoes(lista):
    if len(lista) == 1:
        return [lista]

    resultado = []
    for i in range(len(lista)):
        atual = lista[i]
        restante = lista[:i] + lista[i+1:]
        
        for p in permutacoes(restante):
            resultado.append([atual] + p)

    return resultado

print(permutacoes([1, 2, 3]))