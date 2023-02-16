### Getter and Setter ###
'''
To implement proper encapsulation in Python, we need to use setters and getters. The primary purpose of using getters
and setters in object-oriented programs is to ensure data encapsulation. Use the getter method to access data members
and the setter methods to modify the data members.
'''


class Student:
    def __init__(self, name, age):
        # private member
        self.name = name
        self.__age = age

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, age):
        self.__age = age


stud = Student('Jeeban', 14)
print(stud.get_age())
stud.name = "Dibya"
print(stud.name)
stud.set_age(20)
print(stud.get_age())



# # retrieving age using getter
# print('Name:', stud.name, stud.get_age())
#
## changing age using setter
# stud.set_age(16)
#
# # retrieving age using getter
# print('Name:', stud.name, stud.get_age())