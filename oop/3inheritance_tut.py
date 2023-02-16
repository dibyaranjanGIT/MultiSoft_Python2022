### Inheritance ###
'''
The process of inheriting the properties of the parent class into a child class is called inheritance.
The existing class is called a base class or parent class and the new class is called a subclass or child class
or derived class.

The main purpose of inheritance is the reusability of code because we can use the existing class to create a new class
instead of creating it from scratch
'''


## Single Inheritance ##
# # Base class
# class Vehicle:
#     def __init__(self):
#         print('Inside Vehicle class')
#
#     def vehicle_info(self):
#         return "The vehicle is a four wheeler"
#
# ## Child class
# class Car(Vehicle):
#     def __init__(self):
#         print('Inside Car class')
#
# ## Create object of Car
# car = Car()
# print(car.vehicle_info())


## Multiple Inheritance ##
'''
In multiple inheritance, a class is derived from more than one class. 
The child class, in this case, has features of both the parent classes.
'''
# Parent class 1
# class Person:
#     def person_info(self):
#         print('Inside Person class')
#         return "The person is male and his age is 35"
#
# # Parent class 2
# class Company:
#     def company_info(self):
#         print('Company Info ! ')
#         return "He is belong ABC company"
# #
# # ## Child class
# class Employee(Person, Company):
#     def __init__(self, salary, skill):
#         self.salary = salary
#         self.skill = skill
#     def employee_info(self):
#         print('Inside Employee class')
#         return f"The employee has salary {self.salary} and has skill {self.skill}"
# #
# jeeban =Employee(2000,'PYTHON')
# print(jeeban.company_info())
# print(jeeban.person_info())


## Create object of Employee
# emp = Employee(2000, "Python Dev")
# print(emp.employee_info())

## Multilevel Inheritance ##
'''
In multilevel inheritance, a class that is already derived from another class is derived by a third class. 
So in this way, the third class has all the other two former classes' features and functionalities. 

The syntax looks something like this:
class Parent1:
    pass
class Derived1(Parent1):
    pass
class Derived2(Derived1):
    pass
'''
## Base class
# class Vehicle:
#     def vehicle_info(self):
#         print('Inside Vehicle class')
#
# ## Child class
# class Car(Vehicle):
#     def car_info(self):
#         print('Inside Car class')
#
# ## Child class
# class SportsCar(Car):
#     def sports_car_info(self):
#         print('Inside SportsCar class')

## Create object of SportsCar
# s_car = SportsCar()
# s_car.vehicle_info()

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
# Sports Car can inherits properties of Vehicle and Car
# class SportsCar(Car, Vehicle):
#     def sports_car_info(self):
#         print("Inside SportsCar class")
