def rotacionar(m):
    n = len(m)
    return [[m[n-1-j][i] for j in range(n)] for i in range(n)]

matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(rotacionar(matriz))