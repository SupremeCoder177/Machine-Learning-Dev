# intersection and difference of arrays

import numpy as np

n1 = np.array([10, 20, 30, 40, 50, 60])
n2 = np.array([50, 60, 70, 80, 90])

# prints the common elements in n1 and n2
print(np.intersect1d(n1, n2))

# prints the unique elements to n1
print(np.setdiff1d(n1, n2))

# prints the unique elements to n2
print(np.setdiff1d(n2, n1))