# accessing and changing the shape of a numpy array

import numpy as np

n1 = np.array([[2, 3, 5], [1, 9, 3]])
print(n1.shape)

n1.shape = (3, 2)
print(n1)

# NOTE : you cannot change the shape into something which is impossible 
# 		 that is, if the original shape if a * b then you can only reshape
#		 the array into shapes say x * y where x * y = a * b, because the number
#		 of elements remain the same