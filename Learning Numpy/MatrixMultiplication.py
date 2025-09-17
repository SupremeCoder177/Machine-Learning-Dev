# first let's implement a matrix multiplication class ourselves

from typing import List

def print_arr(arr):
    for i in arr:
        print(i)

class Multiplier:

    def __init__(self): pass

    @staticmethod
    def shape(array : List[List[any]]) -> List[int]:
        return [len(array), len(array[0])]

    def check_compatibility(self, array1 : List[List[any]], array2 : List[List[any]]) -> bool:
        return self.shape(array1)[1] == self.shape(array2)[0]

    def multiply(self, array1 : List[List[any]], array2 : List[List[any]]) -> None | List[List[any]]:
        if not self.check_compatibility(array1, array2):
            print("Incompatible matrix shapes")
            return None
        output = []
        row = 0
        while row < len(array1):
            column = 0
            temp = []
            while column < len(array2[0]):
                var = 0
                for i in range(len(array1[0])):
                    var += array1[row][i] * array2[i][column]
                column += 1
                temp.append(var)
            row += 1
            output.append(temp)
        return output


print("Without using numpy:")
arr1 = [[1, 2, 3], [4, 5, 6]]
arr2 = [[1, 2], [3, 4], [5, 6]]

print("[")
print_arr(arr1)
print("]")
print(" * ")
print("[")
print_arr(arr2)
print("]")
print("=")
mul = Multiplier()
out = mul.multiply(arr1, arr2)
for row in out:
    print(row)

# now with numpy
import numpy as np

print()
print("Now using numpy:")

n1 = np.array([[1, 2, 3], [4, 5, 6]])
n2 = np.array([[1, 2], [3, 4], [5, 6]])
# n3 = np.dot(n1, n2)
n3 = n1 @ n2 # same thing as np.dot
print(n3)



