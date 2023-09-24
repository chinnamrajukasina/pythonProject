import numpy as np

itemsDataArray = np.loadtxt(".\\numpy_data.txt", skiprows=1, dtype=np.int64, delimiter=',')
print(itemsDataArray)

itemsArray1, itemsArray2, itemsArray3 = np.loadtxt(".\\numpy_data.txt", skiprows=1, dtype=np.int64, delimiter=',')
print("the item 1 Array is:", itemsArray1)
print("the item 2 Array is:", itemsArray2)
print("the item 3 Array is:", itemsArray3)
print(itemsDataArray[-1])  # to print the last row in the array matrix

# Add a new row to the data
new_row = [104, 2, 2000]
data = np.vstack([itemsDataArray, new_row], dtype=np.int64)
print("Updated data:")
print(data)  # Print the updated data, not itemsDataArray

np.savetxt(".\\numpy_updatedData.txt", data, fmt='%d')


# Load the updated data with explicit data type as int64
updatedData = np.loadtxt(".\\numpy_updatedData.txt").astype(np.int64)
print(updatedData)
