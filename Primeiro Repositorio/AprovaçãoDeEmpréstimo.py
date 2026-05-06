precoCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salario atual: "))
ano = int(input("Digite em quantos anos pretende pagar a casa: "))
if precoCasa / (12 * ano ) > 0.30 * salario:
    print("Empréstimo negado")
else:
    print("Empréstimo realizado com sucesso")