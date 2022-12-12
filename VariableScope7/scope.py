'''
Local Variable:-
A variable that is declared inside a function or loop is called a local variable.

Global Variable:-
On the other hand, a global variable is easier to understand; it is not declared inside the function and can be accessed
anywhere within a program.
'''

## Local variable
def sum():
    a = 10
    b = 20
    sum = a + b
    print(sum)
# print(a)  # this gives an error

## Global variable
# a=1
# def print_Number():
#     a = a+1;
#     print(a)
#
# print_Number()

'''
In Python, the global keyword allows us to modify the global variable. It is used to create a 
global variable and make changes to the variable in a local scope.
'''

a=1
print(a)
def print_Number():
    global a # by writing global it points to the global which is a = 1
    a = a+10;
    print(a)

print_Number()
print(a)

