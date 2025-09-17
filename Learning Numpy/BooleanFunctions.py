import numpy as np

# create an array of random integer values
arr = np.random.randint(0, 5, size = [5, 10])
print(arr)

# select the first row
arr_at_0 = arr[0]
print(arr_at_0)

# basically this loops over all the elements and checks if the value is == 1
arr_is_1 = arr_at_0 == 1

# and the result we get back is just a boolean array
print(arr_is_1)

# we can chain multiple conditions as well using the bitwise | operator
arr_is_0_or_1 = (arr_at_0 == 1) | (arr_at_0 == 0)
print(arr_is_0_or_1)

# or we can use the other bitwise operators like the & operator
arr_is_greater_than_1 = (arr_at_0 > 1) & (arr_at_0 < 4)
print(arr_is_greater_than_1)