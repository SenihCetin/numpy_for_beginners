import numpy as np

#  Let's see how we can save a NumPy array

array = np.array([[1,2,3], [4,5,6]])
np.save("data", array)

#  NumPy array was saved

#  If you want to save the file on desktop
#  You can use that way:
#  np.save("C:\\User\\Senih\\Desktop\\data", array)

#  Now let's see how we can load a NumPy array

array = np.load("data.npy")
print(array)

#  Save multiple NumPy array

array1 = np.array([[1,2,3], [4,5,6]])
array2 = np.array([[-1,-2,-3], [-4,-5,-6]])

np.savez("data", array1, array2)

#  If you have a lot of data work with
#  you could save your data asa compressed file

array1 = np.array([[1,2,3], [4,5,6]])
array2 = np.array([[-1,-2,-3], [-4,-5,-6]])
array3 = np.array([[1000,2000,3000]])

np.savez_compressed("data2", array1, array2, array3)

# Let's see how to load NumPy arrays

arrays = np.load("data.npz")
array1 = arrays["arr_0"]
array2 = arrays["arr_1"]
array3 = arrays["arr_2"]

print(array1)
print(array2)
print(array3)