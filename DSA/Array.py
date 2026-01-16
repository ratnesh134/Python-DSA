from array import *

val = array("i",[1,2,3,4,5,6])

for i in val:
    print(i, end=" ")


print("\n")
# Better Approach

for i in range(0,len(val)):
    print(val[i],end=" ")

print("\n")

# To find the Typecode of the array

print(val.typecode)

print("\n")

# To reverse the array and print the elements

val.reverse()

for i in range(0,len(val)):
    print(val[i], end=" ")