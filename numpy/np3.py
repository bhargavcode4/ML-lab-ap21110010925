import numpy as np
arr1= np.array([1,22,44,20])

arr2=np.array([[1,22,44,22]])

print(type(arr1))
print(type(arr2))

arr4=np.isin(arr1, arr2)
print(arr4)