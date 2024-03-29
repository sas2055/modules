"""
# Array:
    - An array is a collection of items stored at contiguous memory locations.
    - The idea is to store multiple items of the same type together.
    - A user can treat lists as arrays.
    - array can be handled in Python by a module named array.
    - They can be useful when we have to manipulate only a specific data type values.
    - If you create arrays using the array module, all elements of the array must be of the same type.
-------------------------------------------------------------------------------------

# Creating a Array:
    - Array in Python can be created by importing array module.
    - array(data_type, value_list) is used to create an array with
    data type and value list specified in its arguments.
---------------------------------------------------------------------------------

import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])

# printing original array
print ("The new created array is: ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()

# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# printing original array
print ("The new created array is: ", end =" ")
for i in range (0, 3):
    print (b[i], end =" ")
===================================================================================

# Adding Elements to Array:
     - Elements can be added to the Array by using built-in insert() function.
     - Insert is used to insert one or more data elements into an array.
     - Based on the requirement, a new element can be added at the beginning,
     end, or any given index of array.
     - append() is also used to add the value mentioned in its arguments at the end of the array.
-------------------------------------------------------------------------------------

import array as arr

# array with int type
a = arr.array('i', [1, 2, 3])


print ("Array before insertion: ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()

# inserting array using
# insert() function
a.insert(1, 4)

print ("Array after insertion: ", end =" ")
for i in (a):
    print (i, end =" ")
print()

# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

print ("Array before insertion : ", end =" ")
for i in range (0, 3):
    print (b[i], end =" ")
print()

# adding an element using append()
b.append(4.4)

print ("Array after insertion : ", end =" ")
for i in (b):
    print (i, end =" ")
print()
===============================================================================

# Accessing elements from the Array:
    - In order to access the array items refer to the index number.
    - Use the index operator [ ] to access an item in a array.
    - The index must be an integer.
-------------------------------------------------------------------------------

import array as arr

# array with int type
a = arr.array('i', [1, 2, 3, 4, 5, 6])

# accessing element of array
print("Access element is: ", a[0])

# accessing element of array
print("Access element is: ", a[3])

# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# accessing element of array
print("Access element is: ", b[1])

# accessing element of array
print("Access element is: ", b[2])
======================================================================

# Removing Elements from the Array:
    - Elements can be removed from the array by using built-in remove() function
    but an Error arises if element doesn’t exist in the set.
    - Remove() method only removes one element at a time,
    to remove range of elements, iterator is used.
    - pop() function can also be used to remove and return an element
    from the array, but by default it removes only the last element of the array,
    to remove element from a specific position of the array,
    index of the element is passed as an argument to the pop() method.
------------------------------------------------------------------------------------

import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 5])

# printing original array
print ("The new created array is: ", end ="")
for i in range (0, 5):
    print (arr[i], end =" ")

print ("\r")

# using pop() to remove element at 2nd position
print ("The popped element is: ", end ="")
print (arr.pop(2))

# printing array after popping
print ("The array after popping is: ", end ="")
for i in range (0, 4):
    print (arr[i], end =" ")

print("\r")

# using remove() to remove 1st occurrence of 1
arr.remove(1)

# printing array after removing
print ("The array after removing is: ", end ="")
for i in range (0, 3):
    print (arr[i], end =" ")
========================================================================

# Slicing of a Array:
    - there are multiple ways to print the whole array with all the elements,
    but to print a specific range of elements from the array, we use Slice operation.
    - Slice operation is performed on array with the use of colon(:).
    - To print elements from beginning to a range use [:Index],
    to print elements from end use [:-Index], to print elements from specific
    Index till the end use [Index:], to print elements within a range,
    use [Start Index:End Index] and to print whole List with the use of slicing operation,
    use [:]. Further, to print whole array in reverse order, use [::-1].
--------------------------------------------------------------------------------

import array as arr

# creating a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end =" ")

# Print elements of a range
# using Slice operation
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)

# Print elements from a
# pre-defined point to end
Sliced_array = a[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_array)

# Printing elements from
# beginning till end
Sliced_array = a[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_array)
==========================================================================

# Searching element in Array:
    - In order to search an element in the array we use a python in-built index() method.
    - This function returns the index of the first occurrence of value mentioned in arguments.
-----------------------------------------------------------------------------

import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 2, 5])

# printing original array
print ("The new created array is: ", end ="")
for i in range (0, 6):
    print (arr[i], end =" ")

print ("\r")

# using index() to print index of 1st occurrence of 2
print ("The index of 1st occurrence of 2 is: ", end ="")
print (arr.index(2))

# using index() to print index of 1st occurrence of 1
print ("The index of 1st occurrence of 1 is: ", end ="")
print (arr.index(1))
==================================================================

# Updating Elements in Array:
    - In order to update an element in the array we simply reassign a new value
    to the desired index we want to update.
-----------------------------------------------------------------------

import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 2, 5])

# printing original array
print ("Array before updation: ", end ="")
for i in range (0, 6):
    print (arr[i], end =" ")

print ("\r")

# updating a element in array
arr[2] = 6
print("Array after updation: ", end ="")
for i in range (0, 6):
    print (arr[i], end =" ")
print()
===============================================================================
"""