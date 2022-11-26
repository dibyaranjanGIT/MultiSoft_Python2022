### Constructor ###
'''
A constructor is a special method used to create and initialize an object of a class. This method is defined in the class.
The constructor is executed automatically at the time of object creation.
The primary use of a constructor is to declare and initialize member/ instance variables of a class.
The constructor contains a collection of statements (i.e., instructions) that executes at the time of object creation
to initialize the attributes of an object.
'''


### Variable scope ###
'''
Instance variables: If the value of a variable varies from object to object, then such variables are called instance
    variables.
Class Variables: A class variable is a variable that is declared inside of class, but outside of constructor or
    __init__() method. This variable is shared between all objects of a class

'''

# class Student:
#     school_name = "KC High School"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# student_one = Student('Jeeban', 20)
# print(student_one.name)


### Inheritance ###

# class Polygon:
#     pi = 3.4
#
#     def __init__(self):
#         print("Thsi is polygon class")
#
#
# class Triangle(Polygon):
#
#     def __init__(self):
#         print("This is Triangle class")

# tg = Triangle()
# print(tg.pi)


### Encapsulation ###

'''
Using encapsulation, we can hide an object’s internal representation from the outside. 
This is called information hiding.

Also, encapsulation allows us to restrict accessing variables and methods directly and prevent accidental 
data modification by creating private data members and methods within a class.

Encapsulation is a way to can restrict access to methods and variables from outside of class. 
Whenever we are working with the class and dealing with sensitive data, providing access to all variables used within 
the class is not a good choice.


## Access Modifiers in Python ##
Encapsulation can be achieved by declaring the data members and methods of a class either as private or protected. 
But In Python, we don’t have direct access modifiers like public, private, and protected.
 We can achieve this by using single underscore and double underscores.
 
Public Member: Accessible anywhere from otside oclass.
Private Member: Accessible within the class (__)
Protected Member: Accessible within the class and its sub-classes (_)
'''

class Employee:
    # constructor
    def __init__(self, name, salary):
        # data members
        self.name = name
        self.__salary = salary

emp = Employee('Dibya', 10000)

print('Name:', emp.name)
print('Salary:', emp.__salary) ## Not showing


## Protected member ##
class Company:
    def __init__(self):
        self._project = "Python"

# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()



### Operator Overloading ###
# print(12 + 20)
# print('a' + 'b')
# here + is an example of operator overloading


### Magic method or Dunder method ###

# class Person:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __add__(self, other):
#         return self.name  + other.name
# #
# p1 = Person('Dibya ')
# p2 = Person('Jena')
# print(p1 + p2)
#
# p1 = Person(20)
# p2 = Person(20)
# print(p1 + p2)



### Getter and Setter ###

# class Student:
#     def __init__(self, name, age):
#         # private member
#         self.name = name
#         self.__age = age
#
#     # getter method
#     def get_age(self):
#         return self.__age
#
#     # setter method
#     def set_age(self, age):
#         self.__age = age
#
# stud = Student('Jessa', 14)
#
# # retrieving age using getter
# print('Name:', stud.name, stud.get_age())
#
# # changing age using setter
# stud.set_age(16)
#
# # retrieving age using getter
# print('Name:', stud.name, stud.get_age())



