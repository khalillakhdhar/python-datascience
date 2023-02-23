import numpy as np
arr = np.array([ -1,7,6, 8, 9])
x = np.searchsorted(arr, 3)
print(x)
print(arr)