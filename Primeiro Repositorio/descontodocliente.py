valor = float(input("Digite o valor da compra:"))
if valor > 100:
    print("Você tem direito a um desconto de 10%")
    print("O valor final do produto é:", valor * 0.9)
elif valor < 100:
    print("Nas compras acima de 100 reais, você ganha 10% de desconto!")
