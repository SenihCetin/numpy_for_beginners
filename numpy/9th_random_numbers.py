#Random numbers in NumPy are useful for simulations,
#modeling, applying random transformations, and testing purposes.

import numpy as np

rng = np.random.default_rng()
print(rng.integers(low=1, high=7, size=(3, 4))) # 3x4 array of Ints
print(rng.integers(low=1, high=7))

np.random.seed(seed=1)
print(np.random.uniform(low=-1, high=1, size=(3, 4)))

array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)

fruits = np.array(["🍍", "🍌", "🥥", "🍊", "🍎"])
print(rng.choice(fruits))
print(rng.choice(fruits, size= 3))
print(rng.choice(fruits, size=(3, 3)))