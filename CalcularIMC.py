peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))
 
imc = peso / (altura ** 2)

if imc > 25:
    print("Acima do pesoa ideal!")
else:
    print("Peso dentro da normalidade!")