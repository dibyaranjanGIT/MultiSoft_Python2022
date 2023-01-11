"""
A list in Python is a collection of items which can contain elements of multiple data types,
which may be either numeric, character logical values, etc. It is an ordered collection supporting negative indexing.

A list can be created using [] containing data values.
Contents of lists can be easily merged and copied using python’s inbuilt functions.
"""

sample_list = [1, "Yash", ['a', 'e']]
print(sample_list)

"""
An array is a vector containing homogeneous elements i.e. belonging to the same data type. 
Elements are allocated with contiguous memory locations allowing easy modification, 
that is, addition, deletion, accessing of elements. In Python, we have to use the array module to declare arrays. 

If the elements of an array belong to different data types, an exception “Incompatible data types” is thrown.
"""

import array

sample_array = array.array('i', [1, 2, 3])

# accessing elements of array
for i in sample_array:
    print(i)
