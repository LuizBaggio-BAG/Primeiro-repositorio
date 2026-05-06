nomes_alunos = []
qntd = int(input("Quantos alunos você quer cadastrar"))

for i in range(qntd):
    nome = input("Digite o nome dos alunos")
    nomes_alunos.append(nome)

print("Nomes dos alunos registrados: ")
for nome in nomes_alunos:
    print(nome)