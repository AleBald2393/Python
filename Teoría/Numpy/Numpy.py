NumPy is a Python library used for working with arrays, linear algebra, fourier transform, and matrices. NumPy stands for Numerical Python and it is an open source project. The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

Arrays are very frequently used in data science, where speed and resources are very important.

NumPy is usually imported under the np alias.

It's usually fixed in size and each element is of the same type. We can cast a list to a numpy array by first importing numpy:

# import numpy library

import numpy as np 

# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a

# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

# Enter your code here
type(b)
b.dtype

para cambiar elementos en array
# Assign the first element to 100

c[0] = 100
c

We can change the 5th element of the array to 0 as follows:
# Assign the 5th element to 0

c[4] = 0
c

SLICING 
# Slicing the numpy array

d = c[1:4]
d
