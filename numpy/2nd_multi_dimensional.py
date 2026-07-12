import numpy as np

array = np.array('A')

print(array.ndim)

array = np.array(['a','b','c'])
#It is one dimensional. You can thhink it likes a row.
print(array.ndim)

array = np.array([['a','b','c'],['1','2','3'],['d','e','f']])

print(array.ndim)

#For more readability you can write like under the line:
array = np.array([['a','b','c'],
                  ['1','2','3'],
                  ['d','e','f']])
#Now, we can see it is 3x3 matrix
print(array.ndim)

array = np.array([[['a','b','c'],
                   ['1','2','3'],
                   ['d','e','f']]])
#Also, you can understand the dimension with number of square brackets.
print(array.ndim)

array = np.array([[['a','b','c'],['1','2','3'],['d','e','f']],
                  [['g','h','i'],['4','5','6'],['j','k','l']],
                  [['m','n','o'],['7','8','9'],['p','q','_']]])
#The tuples must have same constant value, otherwise the code will not execute.
#If a tuple does not have a value you can write _ or space.
print(array.ndim)

print(array.shape)
#(depht(layer(s)), the number of rows, number of columns)

#You would access the elements like this:
#Chain Indexing
print(array[0][0][0])
print(array[2][1][2])

#or like this:
#Multidimensional Indexing
print(array[0, 0, 0])
print(array[0, 1, 2])

#Multidimensional Indexing is faster than Chain Indexing

word = array[0, 0, 1] + array[1, 0, 2] + array[1, 0, 0]
print(word)