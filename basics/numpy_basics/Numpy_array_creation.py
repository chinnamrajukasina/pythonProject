import numpy as np


# array creation using literal method
literalArray = np.array([1, 5])
print("firstArray is", literalArray)
print("firstArray dimension is", literalArray.ndim)
print("firstArray size is", literalArray.size)
print("firstArray shape is", literalArray.shape)
print()

# array creation using aRange method
aRangeArray = np.arange(2, 20, 2)
print("aRangeArray is", aRangeArray)
print("aRangeArray dimension is", aRangeArray.ndim)
print("aRangeArray size is", aRangeArray.size)
print("aRangeArray shape is", aRangeArray.shape)
print()

# array creation using ones method
onesArray = np.ones([1, 3, 2], dtype=int)
print("onesArray is\n", onesArray)
print("onesArray dimension is", onesArray.ndim)
print("onesArray size is", onesArray.size)
print("onesArray shape is", onesArray.shape)
print()

# array creation using zeros method
zerosArray = np.zeros([1, 3, 4], dtype=int)
print("zerosArray is\n", zerosArray)
print("zerosArray dimension is", zerosArray.ndim)
print("zerosArray size is", zerosArray.size)
print("zerosArray shape is", zerosArray.shape)
print()

# array creation using onesLike method
onesLikeArray = np.ones_like([1, 3, 4], dtype=int)
print("onesLikeArray is\n", onesLikeArray)
print("onesLikeArray dimension is", onesLikeArray.ndim)
print("onesLikeArray size is", onesLikeArray.size)
print("onesLikeArray shape is", onesLikeArray.shape)
print()

# array creation using zerosLike method
zerosLikeArray = np.ones_like([1, 3, 4], dtype=int)
print("zerosLikeArray is\n", zerosLikeArray)
print("zerosLikeArray dimension is", zerosLikeArray.ndim)
print("zerosLikeArray size is", zerosLikeArray.size)
print("zerosLikeArray shape is", zerosLikeArray.shape)
print()

# array creation using linSpace method
linSpaceArray = np.linspace(1, 4, 4, dtype=int)
print("linSpaceArray is\n", linSpaceArray)
print("linSpaceArray dimension is", linSpaceArray.ndim)
print("linSpaceArray size is", linSpaceArray.size)
print("linSpaceArray shape is", linSpaceArray.shape)
print()

# array creation using random method
randomArray = np.random.random(4)
print("randomArray is\n", randomArray)
print("randomArray dimension is", randomArray.ndim)
print("randomArray size is", randomArray.size)
print("randomArray shape is", randomArray.shape)
print()
