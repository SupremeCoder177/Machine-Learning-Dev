# Normally you cannot add two matrices of different size

import numpy as np

# like
n1 = np.array([np.arange(0, 5), np.arange(5, 10)])
n2 = np.array([[1], [2]])

# if you do
n3 = n1 + n2
# it will not give an error because numpy resizes the n2 array into the shape of n1
# but there is still a limitation, the no. of rows of n1 has to be == no. of rows of n2

print(n1)
print("+")
print(n2)
print("=")
print(n3)

# You will see that the column vector n2 has been added to all the columns of n1
# because numpy changes the n2 array from [[1], [2]] to
#[ [1, 1, 1, 1, 1],
#  [2, 2, 2, 2, 2] ]
