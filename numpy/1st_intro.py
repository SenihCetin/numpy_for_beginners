list = [0,1,2,3,4]

list = list * 2

print(list)
# As you can see, multiplying a standard list repeats its elements.

import numpy as np

array = np.array([0,1,2,3,4])

array = array * 2

print(array)
print(type(array))

# Thanks to NumPy, the multiplication is applied element-wise, giving us multiplied values.