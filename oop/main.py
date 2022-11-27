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
'''
The process of inheriting the properties of the parent class into a child class is called inheritance. 
The existing class is called a base class or parent class and the new class is called a subclass or child class 
or derived class.

The main purpose of inheritance is the reusability of code because we can use the existing class to create a new class 
instead of creating it from scratch
'''


## Single Inheritance ##
# Base class
# class Vehicle:
#     def Vehicle_info(self):
#         print('Inside Vehicle class')
#
# # Child class
# class Car(Vehicle):
#     def car_info(self):
#         print('Inside Car class')
#
# # Create object of Car
# car = Car()


## Multiple Inheritance ##

# # Parent class 1
# class Person:
#     def person_info(self, name, age):
#         print('Inside Person class')
#         print('Name:', name, 'Age:', age)
#
# # Parent class 2
# class Company:
#     def company_info(self, company_name, location):
#         print('Inside Company class')
#         print('Name:', company_name, 'location:', location)
#
# # Child class
# class Employee(Person, Company):
#     def employee_info(self, salary, skill):
#         print('Inside Employee class')
#         print('Salary:', salary, 'Skill:', skill)
#
# # Create object of Employee
# emp = Employee()


## Multilevel Inheritance ##

# # Base class
# class Vehicle:
#     def vehicle_info(self):
#         print('Inside Vehicle class')
#
# # Child class
# class Car(Vehicle):
#     def car_info(self):
#         print('Inside Car class')
#
# # Child class
# class SportsCar(Car):
#     def sports_car_info(self):
#         print('Inside SportsCar class')
#
# # Create object of SportsCar
# s_car = SportsCar()


## Hierarchical Inheritance ##
'''
In Hierarchical inheritance, more than one child class is derived from a single parent class. In other words, 
we can say one parent class and multiple child classes.
'''
# class Vehicle:
#     def info(self):
#         print("This is Vehicle")
#
# class Car(Vehicle):
#     def car_info(self, name):
#         print("Car name is:", name)
#
# class Truck(Vehicle):
#     def truck_info(self, name):
#         print("Truck name is:", name)


## Hybrid Inheritance
'''
When inheritance is consists of multiple types or a combination of different inheritance is called hybrid inheritance.
'''
# class Vehicle:
#     def vehicle_info(self):
#         print("Inside Vehicle class")
#
# class Car(Vehicle):
#     def car_info(self):
#         print("Inside Car class")
#
# class Truck(Vehicle):
#     def truck_info(self):
#         print("Inside Truck class")
#
## Sports Car can inherits properties of Vehicle and Car
# class SportsCar(Car, Vehicle):
#     def sports_car_info(self):
#         print("Inside SportsCar class")


## SUPER Function ##
'''
In child class, we can refer to parent class by using the super() function. The super function returns a
temporary object of the parent class that allows us to call a parent class method inside a child class method.
'''
# class Company:
#     def company_name(self):
#         return 'Google'
#
# class Employee(Company):
#     def info(self):
#         c_name = super().company_name()
#         print("Jessa works at", c_name)
## Or
# class Employee(Company):
#     def info(self):
#         # Calling the superclass method using class name function
#         c_name = Company().company_name()
#         print("Jessa works at", c_name)
#
# emp = Employee()
# emp.info()


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
 
Public Member: Accessible anywhere from outside class.
Private Member: Accessible within the class (__)
Protected Member: Accessible within the class and its sub-classes (_)
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
class Company:
    def __init__(self):
        self._project = "Python"
        self.institute = 'MS'

# # child class
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


### Getter and Setter ###
'''
To implement proper encapsulation in Python, we need to use setters and getters. The primary purpose of using getters 
and setters in object-oriented programs is to ensure data encapsulation. Use the getter method to access data members 
and the setter methods to modify the data members.
'''


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
# stud = Student('Rama', 14)
#
# # retrieving age using getter
# print('Name:', stud.name, stud.get_age())
#
# # changing age using setter
# stud.set_age(16)
#
# # retrieving age using getter
# print('Name:', stud.name, stud.get_age())


### Magic method or Dunder method ###
#
# class Employee:
#     def __init__(self):
#         self.name = 'Swati'
#         self.salary = 10000
#
#     def __str__(self):
#         return 'name ' + self.name + ' salary=$' + str(self.salary)
#
#
# e1 = Employee()
# print(e1)

# class Person:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __add__(self, other):
#         return self.name + other.name
# #
# p1 = Person('Dibya')
# p2 = Person('Jeeban')
# print(p1 + p2)
#
# p1 = Person(20)
# p2 = Person(20)
# print(p1 + p2)

