# Numpy stands for = Numeric Python
# it is used for scientific calculations

import numpy as np

# single dimensional array
n1 = np.array([10, 20, 20, 30, 40])

# multi dimensional array
n2 = np.array([[10, 20, 30, 40], [20, 30, 10 ,30]])

# printing to console
print(n1)
print(type(n1)) # prints numpy.ndarray = numpy n-dimensional array
print(n2)

# making an array of only zeroes
n3 = np.zeros((1, 2)) # 1, 2 is the dimension of the matrix 
n4 = np.zeros((3, 4))

print(n3)
print(n4)

# initializing an array with the same array
n5 = np.full((3, 3), 10) # 3, 3 is the dimension and 10 is the value it is filled with
print(n5)

# initializing an array with only 1's
n6 = np.ones((2, 2, 2)) # creates a 3-dimensional array filled with only 1
print(n6)