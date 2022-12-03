'''
Decorator is something which takes a function as a parameter and add some functionalities to it and returns
the original function
'''

## Note in Python we can pass a function as an argument to another function

# import time
#
# def add_number(x, y):
#     return x + y
#
# def calculate_time(func):
#     start_time = time.time()
#     print(add_number(10, 5))
#     end_time = time.time()
#     print(end_time - start_time)
#
# calculate_time(add_number())



## Nested function = function inside a function

# import time
# def calculate_time(func):
#     def add_number(x, y):
#         return x + y
#     start_time = time.time()
#     print(add_number(10, 5))
#     end_time = time.time()
#     print(end_time - start_time)

## In python we can also create a fucntion which can return another function

# import time
#
# def calculate_time():
#     def add_number(x, y):
#         return x + y
#     return add_number
#
# result = calculate_time()
# print(result(10, 5))


## Now Decorator ##

import time

def add_number(x, y):
    return x + y

def calculate_time(func):
    def time_wrapper(x, y):
        start = time.time()
        print(func(x, y))
        end = time.time()
        return f"Time taken {end - start}"
    return time_wrapper

result = calculate_time(add_number)
# print(result(10,6))

@calculate_time
def substract_number(x, y):
    return x - y

print(substract_number(20001, 102))