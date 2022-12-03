'''
Remeber the LEGB rule

Local namespace
Enclosing Function locals
Global namespace
Built-in Python modules
'''
## Python closure

'''
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
'''

## Nested function
# def number():
#     x = 100
#     def add():
#         print(x)
#     add()
# number()

# Now I am returning the function instead of calling the function
def number():
    x = 100
    def add():
        return x
    return add
result = number()
print(result())

'''
The function "add" has its scope only inside the "number".
But with the use of closures, we can easily extend its scope to invoke a function outside its scope.
'''
