import numpy as np 
salarios = np.array([
    [5000, 4550, 3200],
    [2100, 1250, 1410],
    [3900, 4900, 5200]
])

k = 1.10

aumento_salarios = salarios * k 
print("O aumento do salarios é de: \n ", aumento_salarios )