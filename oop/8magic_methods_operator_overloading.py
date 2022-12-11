
### Magic method or Dunder method ###

class Employee:
    def __init__(self):
        self.name = 'Dibya'
        self.salary = 10000

    def __str__(self):
        return 'name ' + self.name + ' salary ' + str(self.salary)


e1 = Employee()
print(e1)
e2 = Employee()
# print(e1 + e2) # This will give error


# class Person:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __add__(self, other):
#         return self.name + other.name
#
# p1 = Person('Dibya')
# p2 = Person('Jeeban')
# print(p1 + p2)
#
# p1 = Person(20)
# p2 = Person(20)
# print(p1 + p2)

## Which operator can be overloaded
# https://docs.python.org/3/library/operator.html