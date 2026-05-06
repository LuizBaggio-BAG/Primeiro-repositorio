matriz = [
    [5, 0, 3, 8],
    [2, 7, 1, 4],
    [9, 6, 2, 0],
    [3, 5, 8, 1]
]

for i in range(4):
    for j in range(4):
        matriz[i][j] = 1

print("Matriz final:")
for linha in matriz:
    print(linha)