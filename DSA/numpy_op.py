import numpy as np

val = np.array([1,2,3,4],float)

for x in val:
    print(x , end=" ")

print("\n")

# Linspace

val = np.linspace(10,30,5) #linspace(start_number, end_number,number_of_partition)

for x in val:
    print(x)

print("\n")

# Arange

val = np.arange(10,20,2) # arange(start, end, space) Does not include the end.

for x in val:
    print(x)

print("\n")

# full

val = np.full(10,5) # full(size of array, value)

for x in val:
    print(x, end=" ")

print("\n")

# Multi-Dimensional Array

zero = np.array(10)

print(zero)

one = np.array([1,2,3,4])

print(one)

two = np.array([[1,2,3],[5,6,7]])

print(two)

three = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]]])

print(three)

print(three.shape)