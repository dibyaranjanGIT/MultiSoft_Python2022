'''
An object is called iterable if we can get an iterator from it. Most built-in containers in Python like: list, tuple,
string etc. are iterables.

Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element
at a time. It implements the iter method an next method.
'''

my_list = [4, 7, 0, 3]
my_iter_obj = my_list.__iter__()


print(my_iter_obj.__next__())
print(my_iter_obj.__next__())


# my_list = [4, 7, 0, 3]
# my_iter = iter(my_list)
#
#
# print(next(my_iter))
# print(next(my_iter))

'''
A more elegant way of automatically iterating is by using the for loop,
    In fact the for loop can iterate over any iterable
'''
# my_list = [4, 7, 0, 3]
# for number in my_list:
#     print(number)

## Below is the code how for loop works, for loop interanlly creats an iterator object and iterate over it
## using the next method until an StopIteration excpetion raised.

# my_list = [1, 4, 7, 0, 3, 2]
# my_iter = iter(my_list)
# while True:
#     try:
#         print(next(my_iter))
#     except StopIteration:
#         break