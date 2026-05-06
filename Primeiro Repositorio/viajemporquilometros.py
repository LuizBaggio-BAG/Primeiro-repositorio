distancia = float(input("Digite a distancia que deseja percorrer em km: "))

if distancia <= 200:
    print("O valor da passagem será ",distancia * 0.50, "reais")
else:
    print("O valor da passagem será: ",distancia * 0.45, "reais")
    