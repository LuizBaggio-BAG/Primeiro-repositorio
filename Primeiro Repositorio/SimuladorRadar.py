velocidade = int(input("Qual era a velocidade do carro no momento que passou no radar?:"))
if velocidade > 80:
    print("Você foi multado! A multa é de: ", (velocidade - 80) * 7, "R$")
else:
    print("Você não foi multado!")