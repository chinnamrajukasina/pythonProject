# numpy_array_constructor.py
import numpy as np


class ArrayInfo:
    def __init__(self, elements, array_name="npArray"):
        self.array = np.array(elements)
        self.dimension = self.array.ndim
        self.size = self.array.size
        self.shape = self.array.shape

        print(f"given {array_name} is:\n", self.array)
        print(f"given {array_name} dimension is:", self.dimension)
        print(f"given {array_name} size is:", self.size)
        print(f"given {array_name} shape is:", self.shape)
        print()


if __name__ == "__main__":
    # Code that creates instances and prints information about arrays
    ArrayInfo([110], "zeroArray")
    ArrayInfo([1, 2],"1D_Array")
    ArrayInfo([[2, 1, 4], [3, 33, 8]], "2D_Array")
    ArrayInfo([[[2, 1, 3], [3, 3, 3]], [[1, 2, 3],[1, 2, 5]]], "3D_Arry")
