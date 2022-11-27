'''
A Sorting Algorithm is used to rearrange a given array or list of elements according to a
comparison operator on the elements.
The comparison operator is used to decide the new order of elements in the respective data structure
'''

'''
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements 
if they are in the wrong order.
'''
import time

arr = [64, 34, 25, 12, 22, 11, 90, 5, 7, 100, 25, 114, 45, 55, 45, 56, 45, 45, 88, 77]


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


start = time.time()
print(bubbleSort(arr))
end = time.time()
print("Time taken", end - start)
# Python program for implementation of Bubble Sort
#
# def bubbleSort(arr):
#     n = len(arr)
#     swapped = False
#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 swapped = True
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#         if not swapped:
#             return
# bubbleSort(arr)
