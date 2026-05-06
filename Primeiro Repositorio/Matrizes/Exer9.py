matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
soma_diag = sum(matriz[i][i] for i in range(4))
print(soma_diag)
