# How to create method for the object and different types of methods
'''
A method / instance method is a function that “belongs to” an object.
'''
# class Employee():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # If a function is declared inside a class then it is called a method
#     def run(self):
#         return f"{self.name} can run 100 km"
#
# jiban = Employee("Jiban", 20)
# v = jiban.run()
# print(v)



'''
Class methods take cls as a parameter that points to the class and not the object instance when the method is called.
@classmethod returns a class method for function
With the help of class methods, we can change and alter the variables of the class.
'''

# class Employee:
#     no_of_leaves = 8
#     # Constructor
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     @classmethod
#     def change_leave(cls, newleave):
#         cls.no_of_leaves = newleave
#
# jeban = Employee('Jeban', 20, 10000)
# dibya = Employee('Dibya', 30, 30000)
#
# jeban.change_leave(12)
# print(dibya.no_of_leaves)

# jeban.no_of_leaves = 10 # This will create a new instance variable no_of_leaves which is not belongs to the class
# print(dibya.no_of_leaves)

## Static methods
'''
Static method is same as class method bound to a class rather than the objects for that class.
Static method can be called with or without an object for that class .

If we want to create a function which does not take self or cls as an argument we can write a static method.
'''

class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def run(self):
        print("He can run 10 kms")

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @staticmethod
    def printgood(string):
        print("This is good " + string)
#
# dibya = Employee("Dibya", 255, "Instructor")
# jiban = Employee("Jeban", 455, "Student")
#
# jiban.printgood("Jeban") # Accessing the static method with the object
# Employee.printgood("Jeban") # Accesing the static method with the class

'''
The difference between a static method and a class method is:

Static method knows nothing about the class and just deals with the parameters.
Class method works with the class since its parameter is always the class itself.
'''
