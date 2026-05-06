import random


matriz = [[random.randint(1,100) for _ in range(3)] for _ in range(3)]
maior = max(max(linha) for linha in matriz)
print( matriz, "Maior:", maior)
