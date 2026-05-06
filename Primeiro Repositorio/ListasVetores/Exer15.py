def rotacionar(lista, n):
    return lista[-n:] + lista[:-n]

print(rotacionar([1, 2, 3, 4, 5], 2))