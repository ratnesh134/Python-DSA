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