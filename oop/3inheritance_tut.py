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
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')

# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

# Create object of Car
car = Car()


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
# Sports Car can inherits properties of Vehicle and Car
# class SportsCar(Car, Vehicle):
#     def sports_car_info(self):
#         print("Inside SportsCar class")
