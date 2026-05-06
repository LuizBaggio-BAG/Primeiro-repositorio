import numpy as np

ingredientes = np.array([
    [5, 7, 70],
    [6, 7, 9]
])

pedidos = np.array([
    [150, 110,],
    [120, 200],
    [165, 124]
])


print("O total de ingredientes é: \n ", ingredientes @ pedidos)