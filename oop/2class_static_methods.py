'''
Class methods take cls parameter that points to the class and not the object instance when the method is called.
@classmethod returns a class method for function
With the help of class methods, we can change and alter the variables of the class.
'''

# class Employee:
#     no_of_leaves = 8
#
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

## Static methods
'''
Static method is bound to a class rather than the objects for that class.

There are few limitations related to static methods, such as:
    Unlike, class method, a static method cannot alter or change any variable value or state of the class.
    Static methods do not have any knowledge related to the class.
'''


class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @staticmethod
    def printgood(string):
        print("This is good " + string)

dibya = Employee("Dibya", 255, "Instructor")
jiban = Employee("Jeban", 455, "Student")

Employee.printgood("Jeban")


