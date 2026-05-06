matriz = [[1,2,3],[4,5,6],[7,8,9]]
k = 2
resultado = [[elem * k for elem in linha] for linha in matriz]
print(resultado)