
## SUPER Function ##
'''
In child class, we can refer to parent class by using the super() function. The super function returns a
temporary object of the parent class that allows us to call a parent class method inside a child class method.
'''
class Company:
    def company_name(self):
        return 'MultiSoft'

class Employee(Company):
    def info(self):
        c_name = super().company_name()
        print("Jeeban works at", c_name)
# Or
class Employee(Company):
    def info(self):
        # Calling the superclass method using class name function
        c_name = Company().company_name()
        print("Jeeban works at", c_name)

emp = Employee()
emp.info()