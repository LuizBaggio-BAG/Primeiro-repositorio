a = []
i = 0 
while i < 10:
    numero = int(input("Digite um numero inteiro: "))
    a.append(numero)
    i = i + 1

print(f"O menor valor é: {min(a)}")
print(f"O maior valor é: {max(a)}")