"""
1. element present at a particular index

1000 elements in the below array
[1,5,2,8,9]

Find the element present on 500th index
here the time complexity O(1)


2. Array of 1000 elements, find the elements which are duplicates
Brute force approach:
    run a for loop and find the count of each element in the list

if the array is sorted then we can just compare the current element with next element to find the duplicates
which will result in O(n) - Linear time complexity

Sorting can be performed in two ways
    1.Quick sort
    2. Merge sort

O(1) - Constant time
O(log n) - Logarithim time
O(n) - Linear time
O(n2) - Quadratic time
O(n3) - Cubic time
O(2n) - Exponential time
"""