nota = float(input("Digite sua nota:"))
if nota >= 9.0:
    print("Parabens, você foi aprovado!!")
elif nota > 7.0 and nota < 8.9:
    print("Aprovado!")
elif nota > 4.0 and nota < 6.9:
    print("Você esta de recuperação!")
else: 
    print("Você foi reprovado")
