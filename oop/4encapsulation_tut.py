### Encapsulation ###
'''
Using encapsulation, we can hide an object’s internal representation from the outside.
This is called information hiding.

Also, encapsulation allows us to restrict accessing variables and methods directly and prevent accidental
data modification by creating private data members and methods within a class.

## Access Modifiers in Python ##
Encapsulation can be achieved by declaring the data members and methods of a class either as private or protected.
But In Python, we don’t have direct access modifiers like public, private, and protected.
 We can achieve this by using single underscore and double underscores.

Public Member: Accessible anywhere from outside class.
Private Member: Accessible within the class ('__')
Protected Member: Accessible within the class and its sub-classes ('_')
'''


# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # data members
#         self.name = name
#         self.__salary = salary
#
# emp = Employee('Jeeban', 10000)
#
# print('Name:', emp.name)
# print('Salary:', emp.__salary) ## Not showing


## Protected member ##

# class Company:
#     def __init__(self):
#         self._project = "Python"
#         self.institute = 'MS'
## child class
# class Employee(Company):
#     def __init__(self, name):
#         self.name = name
#         Company.__init__(self)
#
#     def show(self):
#         print("Employee name :", self.name)
#         print("Working on project :", self._project)
#
# e = Employee("Jeeban")
# e.show()
# print(e._project)