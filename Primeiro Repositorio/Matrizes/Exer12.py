def eh_simetrica(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            if m[i][j] != m[j][i]:
                return False
    return True

matriz = [[1,2,3],[2,5,6],[3,6,9]]
print(eh_simetrica(matriz))