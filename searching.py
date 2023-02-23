import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 6])
x = np.where(arr %3==0)
print(x)
arr=np.append(arr,[8])
print(arr)