import numpy as np

estoque_inicial = np.array([[
    [2000, 250, 650],
    [3000, 1000, 500],
    [150, 200, 150]
]])

vendas = np.array([
    [1500, 150, 300],
    [2350, 670, 340],
    [35, 175, 67]
])

estoque_final = estoque_inicial - vendas
print(f"O estoque inicial era de: \n ", estoque_inicial)
print(f"O total de venda foi de: \n", vendas)
print(f"O estoque atual é de: \n ", estoque_final)