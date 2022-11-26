# Q1.
# Create a function which can take n number of arguments and return the sum of it
# Hint - Use the concept of *args

# def sum(*args):
#     res = 0
#     for i in args:
#         res = i+res
#         return res
#     return sum(args)
# x = sum(5,6,10)
# print(x)

# Q2.
# Create a function to which will take two arguments and returns the result by division
# 	1. If the user did not give any input the function should have a default value of 1 for both the parameter
# 	2. Also Try to handle division by zero error using Try Except clause

# def division(x1=1,y1=1):
#     try:
#         res = x1/y1
#         return res
#     except ZeroDivisionError as e:
#         return e
#
# x = division(12,0)
# print(x)

#
# Q3.
# Create a lambda function which will generate a list of even numbers
# Hint: Use map or filter function to see the result of a lambda function
#

# li = [1,2,3,4,5,6]
# print(list(filter(lambda n : n%2 == 0, li)))

# def mul(n):
#     return n*n
#
# print(list(map(mul, [2,4])))

# Q4.
# Create a function which will take a list of numbers as argument and returns the highest number in that list
# li = [12, 115, 56, 58, 95]
# def number(li):
#     highest_num = li[0]
#     for i in li[1:]:
#         if i > highest_num:
#             highest_num = i
#
#     return highest_num
# x1 = number(li)
# print(x1)


# Q5.
# Write a function to remove characters from a string starting from zero up to n and return a new string.
# and returns a string.
# input : string , n : number of characters to remove

def main(str1,n):
    x = str1[n:]
    return x
new_str = main("Jeeban",2)
print(new_str)


# Q6.
# Create a function which take a tuple as input and check whether all the items in the tuple are equal or not
