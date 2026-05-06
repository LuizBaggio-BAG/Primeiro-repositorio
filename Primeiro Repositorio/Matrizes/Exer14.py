def multiplicar(A, B):
    linhas_A = len(A)
    colunas_A = len(A[0])
    colunas_B = len(B[0])

    resultado = [[0]*colunas_B for _ in range(linhas_A)]

    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(colunas_A):
                resultado[i][j] += A[i][k] * B[k][j]
    return resultado

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
print(multiplicar(A, B))