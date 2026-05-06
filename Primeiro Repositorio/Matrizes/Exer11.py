matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
soma_colunas = [sum(matriz[i][j] for i in range(3)) for j in range(3)]
print(soma_colunas)