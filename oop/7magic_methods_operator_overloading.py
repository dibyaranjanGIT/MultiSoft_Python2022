"""
Magic methods are special methods in python that have double underscores (dunder) on both sides of the method name.

Use the dir() function to see the number of magic methods
dir(int)
"""
### Magic method or Dunder method ###

# class Employee:
#     def __init__(self):
#         self.name = 'Dibya'
#         self.salary = 10000
#
#     def __str__(self):
#         return 'This belongs to Employee class'
#
#
# e1 = Employee()
# print(e1)

## Example2
#
# class Person:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __add__(self, other):
#         return self.name + other.name
#
# p1 = Person('Dibya ')
# p2 = Person('Jeeban')
# print(p1 + p2)
#

# abc = 123
# print(dir(abc))