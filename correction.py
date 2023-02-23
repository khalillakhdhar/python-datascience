import numpy as np
arr = np.array([])
while len(arr)<4:
    e=int(input("donnez un entier "))
    u=e%10
    if(u==0 or u==10):
        arr=np.append(arr,e)
x=int(input("donnez un entier pour chercher son indice trié? "))
indice=np.searchsorted(arr,x)
print(arr)
print("la bonne position pour %s est %s "%(x,indice))