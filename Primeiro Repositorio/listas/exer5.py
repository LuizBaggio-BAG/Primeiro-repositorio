numeros = []
par = []
impar = []
for i in range(5):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

if len(par) !=0:
      print(max(par))
else:
     print("Não foi digitado nenhum valor par: ")
if len(impar) != 0:
      print(min(impar))
      
else:
    print("Nenhum número impar foi digitado") 
print(sum(numeros))
print(sum(numeros)/len(numeros))