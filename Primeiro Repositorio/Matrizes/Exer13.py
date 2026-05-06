matriz = [[i + j*5 for i in range(5)] for j in range(5)]
diag_sec = [matriz[i][4-i] for i in range(5)]
print(diag_sec)