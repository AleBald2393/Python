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

# Set the fourth element and fifth element to 300 and 400

c[3:5] = 300, 400
c
We can also define the steps in slicing, like this: [start:end:step].
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

#print the even elements
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Enter your code here
print  (arr[1:8:2])

# Create the index list

select = [0, 2, 3, 4]
select

# Get the size of numpy array

a.size

# Get the number of dimensions of numpy array

a.ndim

# Get the shape/size of numpy array

a.shape

# Get the mean of numpy array

mean = a.mean()
mean

# Get the standard deviation of numpy array

standard_deviation=a.std()
standard_deviation

# Get the biggest value in the numpy array

max_b = b.max()
max_b

# Get the smallest value in the numpy array

min_b = b.min()
min_b

# Numpy Array Addition

z = np.add(u, v)
z

# Plotting functions


import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt


def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

# Plot numpy arrays

Plotvec1(u, z, v)

c = np.subtract(a, b)

print(c)

# Numpy Array Multiplication

z = np.multiply(x, y)
z

c = np.divide(a, b)
c

# Calculate the dot product

np.dot(X, Y)

# Add the constant to array

u + 1

# The value of pi

np.pi

# Create the numpy array in radians

x = np.array([0, np.pi/2 , np.pi])

# Calculate the sin of each elements

y = np.sin(x)
y

Linspace
A useful function for plotting mathematical functions is linspace. Linspace returns evenly spaced numbers over a specified interval.

    numpy.linspace(start, stop, num = int value)

start : start of interval range

stop : end of interval range

num : Number of samples to generate.

# Makeup a numpy array within [-2, 2] and 5 elements

np.linspace(-2, 2, num=5)

# Make a numpy array within [-2, 2] and 9 elements

np.linspace(-2, 2, num=9)

# Plot the result

plt.plot(x, y)

Iterating 1-D Arrays
Iterating means going through elements one by one.

If we iterate on a 1-D array it will go through each element one by one.
If we execute the numpy array, we get in the array format

# Import the libraries

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt


def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

# Write your code below and press Shift+Enter to execute
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
#Starting index in slice is 1 as first even element(2) in array1 is at index 1
even_arr1 = arr1[1:5:2]
print("even for array1",even_arr1)
    
#Starting index in slice is 0 as first odd element(1) in array1 is at index 0
odd_arr1=arr1[0:5:2]
print("odd for array1",odd_arr1)

#Starting index in slice is 0 as first even element(6) in array2 is at index 0
even_arr2 = arr2[0:5:2]
print("even for array2",even_arr2)
    
    
#Starting index in slice is 1 as first odd element(7) in array2 is at index 1
odd_arr2=arr2[1:5:2]
print("odd for array2",odd_arr2)
