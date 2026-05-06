lista = [1, 2, 2, 3, 4, 3, 5]
sem_duplicatas = []
for x in lista:
    if x not in sem_duplicatas:
        sem_duplicatas.append(x)
print(sem_duplicatas)