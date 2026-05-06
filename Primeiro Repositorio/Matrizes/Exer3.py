matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
num = 7
encontrado = any(num in linha for linha in matriz)
print("num", encontrado)