import numpy as np

# Scalar Arithmetic

array = np.array([0,1,2,3])
print(array + 2)
print(array - 2)
print(array * 2)
print(array / 2)
print(array ** 2)
print(array // 2)

# Vectorized Math Functions

print(np.sqrt(array))
print(np.exp(array))

arr = np.array([1.01,2.76,3.99])

print(np.round(arr))
print(np.ceil(arr))
print(np.floor(arr))

# Element-Wise Arithmetic

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 // array2)
print(array1 ** array2)

# Comparison Operators

scores = np.array([100,20,45,53,75,80,99])

print(scores == 100)
print(scores >= 60)

scores[scores <= 60] = 0
print(scores)