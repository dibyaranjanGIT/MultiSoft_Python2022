# Class = Class is a template or blueprint from which we cretes object
# Object/ instance = It is an instance of the class
# Attribute/ instance variable/ member variable/ data meember = The characterstics associated with a object
# Method/ Instance method = The function inside a class
#
# class Employee:
#     pass
#
# dibya = Employee()
# dibya.fname = "Dibyaranjna"
# dibya.age = 30
#
#
# jeban = Employee()
# jeban.fname = "Jeeban"
# jeban.age = 20
#
# print(jeban.fname)

## To reduce this code we can create a Constructor insdie a class
## Constructor ##
'''
A constructor is a special method used to create and initialize an object of a class. 
The primary use of a constructor is to declare and initialize member/ instance variables of a class.
The constructor is executed automatically at the time of object creation.
'''
#
# class Employee:
#     def __init__(self, fname, age):
#         self.fname = fname
#         self.age = age
# jiban = Employee("jeeban", 21)
# print(jiban.age)

# dibya = Employee("Dibya", 30)
# print(dibya.fname)


class Employee:
    def __init__(self):
        print("This is an employee class")

jiban = Employee()











