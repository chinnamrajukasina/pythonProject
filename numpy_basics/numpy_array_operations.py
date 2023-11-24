import numpy as np
from numpy_array_constructor import ArrayInfo

ArrayInfo([11, 44], "1D_Array")

array1 = np.array([[12, 13], [22, 33]])
array2 = np.array([[11, 22], [22, 33]])
myTuple = np.array(((2, 2), (3, 3)))
arraySum = array1 + array2
arrayProduct = array1 * array2
ArrayInfo(arraySum)
ArrayInfo(arrayProduct)
ArrayInfo(array1 / myTuple)  # division of an Array with tuple is an Array

onesArray = np.ones([4, 2], dtype=np.int32)
zerosArray = np.zeros((4, 1), dtype=np.int32)
concatArray = np.concatenate([onesArray, zerosArray], axis=1)
ArrayInfo(concatArray, "concatArray")

ArrayInfo(np.sort(concatArray, axis=1))  # array sort

ArrayInfo(np.sort(array1)[::-1]) # reverse sort

ArrayInfo(np.eye(3))  # identity Matrix

ArrayInfo(onesArray.transpose())  # transpose
