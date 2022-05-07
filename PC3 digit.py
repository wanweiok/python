import numpy as np
import cmath
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
b = [2+3j, 4+5j, 6-7j, 8+9j]
print(b)
print(cmath.sin(b[0]))
print(a)
print(np.sin(a))

grid = np.zeros(shape=(10000,10000), dtype=float)
print(grid)
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[1:3,1:3])
print(a)
b = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
print(b*b.I)

import random, datetime
random.seed(datetime.datetime.now())
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))