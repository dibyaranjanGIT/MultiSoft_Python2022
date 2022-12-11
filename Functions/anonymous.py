'''
What is Anonymous function?
In Python programming, an anonymous function or lambda expression is a function definition that is not bound to
an identifier (def).

The anonymous function is an inline function. The anonymous functions are created using a lambda keyword.
'''

## Lambda functions or anonymous functions
def add(a, b):
    return a+b

minus = lambda x, y: x+y

## Lambda function with if else
result = lambda x : x if x%2==0 else 0