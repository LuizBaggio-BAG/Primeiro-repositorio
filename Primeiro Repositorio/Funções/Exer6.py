def par_ou_impar(a):
    if a % 2 == 0: 
        return "Par"
    else: 
        return "Ímpar"
a = int(input("Digite um número e verifique se ele é par ou ímpar:"))
print(f"O número ({a}) é {par_ou_impar(a)}")