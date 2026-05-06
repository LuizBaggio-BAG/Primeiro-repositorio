qntd = int(input("Digite o número de alunos na sala: "))
cont = 0
cont2 = 0
a = []
for i in range(qntd):
    nota = int(input("Digite a nota dos alunos: "))
    a.append(nota)
    if nota >= 60:
        cont += 1
    else:
        cont2 += 1 
print("A quantidade de alunos na média ou acima da média é: ", cont)
print("A quantidade de alunos abaixo da média é: ", cont2)