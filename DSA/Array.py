from array import * # imports all the modules inside array package

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

print("\n")

# Insertion of element

val.insert(1,50) #inserts the element at a 1st index position

val.append(100) # inserts the element at the end of the array

val[2] = 200 # overide the value at 2nd index position

for i in range(0,len(val)):
    print(val[i],end=" ")

print("\n")
# To copy array to another variable

copy_arr = array(val.typecode,[x for x  in val])

for i in range(0,len(copy_arr)):
    print(copy_arr[i],end=" ")


print("\n")
# To delete the element from array

copy_arr.pop(3) # Here mention the index position

for i in range(0,len(copy_arr)):
    print(copy_arr[i],end=" ")