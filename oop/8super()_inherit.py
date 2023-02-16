
## SUPER Function ##
'''
In child class, we can refer to parent class methods by using the super() function.
The super function returns a temporary object of the parent class that allows us to call a parent class method inside a
child class method.
'''
# class Company:
#     def company_name(self):
#         return 'MultiSoft'
#
# class Employee(Company):
#     def info(self):
#         c_name = super().company_name()
#         print("Jeeban works at", c_name)
#
# #
# emp = Employee()
# emp.info()
#
# ## Example2.
# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def area(self):
#         return self.x * self.y
#
# class Square(Shape):
#     def __init__(self, x):
#         super().__init__(x, x)
#
# s = Square(4)
# print(s.area())
