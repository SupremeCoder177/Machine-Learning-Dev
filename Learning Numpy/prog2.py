# initializing arrays in a range

import numpy as np

# initialized an array from 10 (inclusive) to 20 (exclusive)
n1 = np.arange(10, 20)
print(n1)

# adding a step to the range
n2 = np.arange(10, 100, 5)
print(n2)

"""
Data types in numpy
Unlike python lists which can store any type of values
numpy arrays only store static data types, i.e. the type of each element is the same

Possible data types for numpy arrays

Integer (int) : int8, int16, int32, int64
Unsigned Integer (uint) : uint8, uint16, uint32, uint64
boolean (bool) : Bool
floating point (float) : float16, float32, float64, float128
complex (complex) : complex64, complex128, complex256
"""

# object hold the list we pass in the initializer of an array
n3 = np.array(object = [1, 12, 45], dtype = "uint32")

# so right now size and shape will be 0
print(n3.size)
print(n3.shape)

# we can convert a numpy array back to a list like so
tmp = n3.tolist()
print(tmp)

