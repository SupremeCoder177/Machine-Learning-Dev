# adding and summing arrays in numpy

import numpy as np

n1 = np.array([10, 20])
n2 = np.array([30, 40])
n3 = np.array([20, 30, 40])

# prints the sum of all the elements inside n1 and n2
print(np.sum([n1, n2]))

# prints the sum of the column vectors into a row vector
print(np.sum([n1, n2], axis = 0))

# prints the sum of the row vector into a row vector
print(np.sum([n1, n2], axis = 1))

# the dimension must be the same for this function to work
try:
	print(np.sum([n1, n2, n3])) 
	print(np.sum([n1, n3], axis = 0))
except Exception as e:
	print("an error has occurred")
