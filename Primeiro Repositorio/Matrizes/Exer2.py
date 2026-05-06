def identidade(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

print("2:")
for linha in identidade(4):
    print(linha)
