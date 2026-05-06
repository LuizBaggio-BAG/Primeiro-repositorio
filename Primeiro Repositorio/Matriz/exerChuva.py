import numpy as np 

manha = np.array([
    [15, 7, 10],
    [30, 12, 6],
    [11, 5, 8]
    ])

tarde = np.array([
    [13, 10, 16],
    [12, 14, 16],
    [9, 3, 4]
])
A = manha + tarde 
print("A quantidade de chuva pela manhã (em mm) foi de:\n ", manha)
print("A quantidade de chuva pela tarde (em mm) foi de: \n ", tarde)
print(f"A quantidade de chuva total (em mm) por região foi de: \n {manha + tarde}")