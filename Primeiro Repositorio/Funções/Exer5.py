def div(a, b):
    quociente = a // b 
    resto=  a % b 
    return quociente, resto 
resultado = div(10, 3)
print(f"quociente: {resultado[0]}, resto: {resultado[1]}")