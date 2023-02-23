from numpy import random as rd
import numpy as np
x = rd.randint(100)
arr=np.array(x)
for i in np.nditer(arr):
    print(i,end=', ')

#chiffre entier aléatoire
print(x)
#y=rd.random(round(6.7))
y=rd.rand()
z=rd.randint(10,size=(6,2))
for i in np.nditer(z):
    print(i,end=', ')
w=rd.choice([2,4,5,6])
print(w)