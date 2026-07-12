import numpy as np

# zeroes function

array1 = np.zeros(10)
print(array1)

array2 = np.zeros((2, 10))
print(array2)

array3 = np.zeros((2, 3, 10))
print(array3)

array4 = np.ones((2, 3, 10))
print(array4)

array5 = np.full((2, 3, 10), 12)
print(array5)

array6 = np.eye(3)
# It executes identity matrix
print(array6)

array7 = np.empty((2, 3))
print(array7)

array8 = np.arange(0, 10, 2) # start, stop, step
print(array8)

array9 = np.linspace(0, 10, 3) # start, stop, num
print(array9)