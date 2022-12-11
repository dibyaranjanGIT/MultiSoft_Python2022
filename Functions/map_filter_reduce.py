'''
map(), filter, and reduce() in Python. These functions are most commonly used with Lambda function.
"Lambda functions are functions that do have any name".
'''

## SYNTAX:
# map(function, iterable)

items = [1, 2, 3, 4, 5]
even_number=list(map((lambda x: x**2), items))
print(even_number)


'''
A filter function in Python tests a specific user-defined condition for a function and returns an iterable for 
the elements and values that satisfy the condition or, in other words, return true.
'''

## SYNTAX:
# filter(function, iterable)

a = [1,2,3,4,5,6]
b = [2,5,0,7,3]
c= list(filter(lambda x: x in a, b))
print(c)