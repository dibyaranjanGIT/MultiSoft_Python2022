### Variable scope ###
'''
Instance variables: If the value of a variable varies from object to object, then such variables are called instance
    variables.
Class Variables: A class variable is a variable that is declared inside of class, but outside of constructor or
    __init__() method. This variable is shared between all objects of a class

'''

class Student:
    school_name = "KC High School" # This is a class variable
    def __init__(self, name, age):
        self.name = name
        self.age = age

student_one = Student('Jeeban', 20)
print(student_one.name)


