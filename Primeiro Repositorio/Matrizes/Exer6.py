matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

pares = sum(1 for linha in matriz for x in linha if x % 2 == 0)
print(pares)
