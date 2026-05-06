temp = float(input("Digite um temperatura em Celsius"))

opcao = str(input("Quer coverter para Fahrenheit(F) ou Kelvin(K)?")).lower().strip()

if opcao == "f":
    print("A conversão para F é: ", (temp * 9/5)+ 32)
elif opcao == "k":
    print("A conversão para K é:", temp + 273,15)