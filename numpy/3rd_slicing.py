import numpy as np

array = np.array([[1 ,2 ,3 ,4],
                  [5 ,6 ,7 ,8],
                  [9 ,10 ,11 ,12],
                  [13 ,14 ,15 ,16]])

#For slicing there is 3 way.

#array[start index : end index : step
print(array[0])
print(array[1])
print(array[-1])          #It will print last row
print(array[0 : 2])       #It gives 0 through 1 not 2. Because the ending index is exclusive.
print(array[3 : 4])       #To see last row we have to write one more than the last index.
print(array[0 : 4 : 2])
print(array[:: -1])
#array[start row's index : end row's index, start column's index : end column's index : step]
print(array[0 : 2, 1 : 3])
print(array[: ,::2])
print(array[:: , 1::2])
print(array[:: , ::-1])
