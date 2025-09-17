# stacking arrays

import numpy as np

n1 = np.array([10, 20, 30])
n2 = np.array([40, 50, 60])

# stacks n1 on top of n2, that is create a 2-dimensional array and puts n1 at row 1
print(np.vstack((n1, n2)))

# stacks the arrays on the same row
print(np.hstack((n1, n2)))

# converts the arrays into column vectors and stacks them side by side
print(np.column_stack((n1, n2)))


# multidimensional stacking
n3 = np.array([[1, 2, 3], [2, 3, 4]])
n4 = np.array([[2, 5, 7], [8, 3, 5]])

print(np.vstack((n3, n4)))

print(np.hstack((n3, n4)))

print(np.column_stack((n3, n4)))