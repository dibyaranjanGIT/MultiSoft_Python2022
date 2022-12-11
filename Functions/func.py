'''
Functions in Python can be defined as lines of codes that are built to create a
specific task and can be used again and again in a program when called.

There are two types of functions in the Python language:

Built-in functions
User-defined functions
'''

# a = 9
# b = 8
# c = sum((a, b)) # built in function

def print_hello():
    print("Hello")

'''
Argument Passing for Python Functions
1. Pass by reference
2. Pass by value
'''

def print_name(name):
    print(f"Your name is {name}")

print_name(name="Jena") # pass by value
print_name("Jena") # Pass by reference

# Default value
def print_name(name=''):
    print(f"Your name is {name}")

## passing multiple argument to the function
def function1(a, b):
    print("Hello you are in function 1", a+b)

'''
Docstring is a short form of documentation string. 
Its purpose is to give the programmer a brief knowledge about the functionality of the function
'''
def function2(a, b):
    """
    This is a function which will calculate average of two numbers
    this function doesnt work for three numbers
    """
    average = (a+b)/2
    # print(average)
    return average

# v = function2(5, 7)
# print(v)
