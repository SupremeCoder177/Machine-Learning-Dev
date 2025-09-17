# some useful functions for arrays

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
# NOTE : transposing can change the shape of the matrix
# print(np.transpose(n2))
print(n2.T) # same thing as np.transpose

# multiplying
# print(n2.dot(n3))

# saving arrays
np.save("dummy", n2.dot(n3))

# loading arrays
n4 = np.load("dummy.npy")
print(n4)

# slicing arrays using the [] selector
"""
Syntax: array[row, column] to select a single cell
        array[row] to select a single row
        array[:row] to select all rows until 'row'
        array[:row, column] selects all values from 0 → row and 0 → column
        array[row_start_index : row_end_index, column] 
"""

n5 = np.random.rand(5, 5)

# row selector
print()
print(n5[:4]) # selects every row except the last one

# column selector
print()
print(n5[: ,-1]) # selects everything in the last row

# universal selector
print()
print(n5[:]) # selects everything

print()
print(n5[:1, -2])
# element from the given column
print()
print(n5[:3, -3]) # so this prints three elements starting from 0 in the third last row

# column selection with starting_row_index != 0
print()
print(n5[2: 4, -2])

# row selection with starting index != 0
print()
print(n5[2:4])

# selecting a single cell
print()
print(n5[3, 2]) 