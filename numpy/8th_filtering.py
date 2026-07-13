#  Filtering = Refers to the process of selecting elements
#              from an array that match a given condition

import numpy as np

ages = np.array([[15, 16, 19, 26, 29, 30, 68],
                 [18, 12, 24, 25, 95, 31, 67]])

teenagers = ages[ages < 18]
print(teenagers)

adults = ages[(ages >= 18) & (ages < 65)]
print(adults)

seniors = ages[ages >= 65]
print(seniors)

evens = ages[ages % 2 == 0]
print(evens)

odds = ages[ages % 2 != 0]
print(odds)

adults = np.where(ages >= 18, ages, 0)
print(adults)