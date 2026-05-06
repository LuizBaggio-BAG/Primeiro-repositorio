lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
intersecao = []

for x in lista1:
    if x in lista2 and x not in intersecao:
        intersecao.append(x)
print(intersecao)