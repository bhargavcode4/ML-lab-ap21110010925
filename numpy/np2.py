import numpy as np
nums = np.array([[3, 332, np.nan, 1],
                 [810, 712,np.nan, 9]])
print(" array with missing values:")
print(nums)
print("array:")
print(np.isnan(nums))

""" isnall or isnull returns a bolean values where missing values
present return true else False"""
