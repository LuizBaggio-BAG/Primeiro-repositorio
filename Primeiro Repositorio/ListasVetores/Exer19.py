def kadane(lista):
    max_atual = max_global = lista[0]

    for i in range(1, len(lista)):
        max_atual = max(lista[i], max_atual + lista[i])
        if max_atual > max_global:
            max_global = max_atual

    return max_global

print(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))