# some usefule functions for arrays

import numpy as np

n1 = np.array([10, 20, 40])
n2 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
n3 = np.full((3, 2), 10)

median = np.median(n1)
standard_deviation = np.std(n1)

print(median, standard_deviation)

# this selects the 3rd column
print(n2[:,2])

# transposing
print(np.transpose(n2))

# multiplying
# print(n2.dot(n3))

# saving arrays
np.save("dummy", n2.dot(n3))

# loading arrays
n4 = np.load("dummy.npy")
print(n4)