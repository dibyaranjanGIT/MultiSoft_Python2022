# Class = Class is a template or blueprint from which we cretes object
# Object = It is an istance of the class
# Attribute = The characterstics associated with a object
# Method = The function inside a class

class Employee:
    pass

dibya = Employee()
dibya.fname = "Dibyaranjna"
dibya.age = 30

jeban = Employee()
jeban.fname = "Jeeban"
jeban.age = 20

print(dibya.name)

## To reduce this code we can create a Constructor insdie a class
## Constructor ##
'''
A constructor is a special method used to create and initialize an object of a class. 
The primary use of a constructor is to declare and initialize member/ instance variables of a class.
The constructor is executed automatically at the time of object creation.
'''

class Employee:
    def __init__(self, fname, age):
        self.fname = fname
        self.age = age

dibya = Employee("Dibya", 30)
print(dibya.fname)












