# initializing arrays with random numbers

import numpy as np

# just printing random integers
print(np.random.randint(10)) # 10 is exclusive

# creating a 1-dimensional array with random integer values
# syntax
n1 = np.random.randint(1, 100, 5)
print(n1)


# creating a multidimensional array with random integer values
n2 = np.random.randint(10, size=(2, 2))
print(n2)

# creating a multidimensional array with random values ranging from 0 to 1 (floating point)
n3 = np.random.rand(5, 5)
print(n3)
# seeing the data type of n3
print(n3.dtype)


