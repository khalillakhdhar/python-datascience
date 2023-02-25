import numpy as np 

x = np.random.randint(5,100, size=(4,5))
arr= np.array(x)
print(arr)
print("éléments paires:")
print(arr[arr%2==0])