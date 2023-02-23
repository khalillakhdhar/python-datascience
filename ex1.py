import numpy as np
tab = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x=int(input("donner x"))
inf = tab[tab < x]
sup = tab[tab > x]
print("Tableau inf :", inf)
print("Tableau sup :", sup)