import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

arr3=[]
for i in range(len(arr1)):
    print(arr1[i]*arr2[i])
    arr3.append(arr1[i]*arr2[i])
    
print(type(arr3))

arr4=np.array(arr3)
print(arr4)
print(type(arr4))