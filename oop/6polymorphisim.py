'''
Polymorphism in Python is the ability of an object to take many forms. In simple words,
polymorphism allows us to perform the same action in many different ways.

The built-in function len() calculates the length of an object depending upon its type. If an object is a string,
it returns the count of characters, and If an object is a list, it returns the count of items in a list

len("Python") # returns 6 as result
len([1,2,3,4,5,6,7,8,9]) # returns 9 as result

'''

# Example
# print(5 + 6)
# print("DIbya" + "Good")

class Rabbit():
    def age(self):
        print("This function determines the age of Rabbit.")

    def color(self):
        print("This function determines the color of Rabbit.")


class Horse():
    def age(self):
        print("This function determines the age of Horse.")

    def color(self):
        print("This function determines the color of Horse.")


obj1 = Rabbit()
obj2 = Horse()
for obj in (obj1, obj2):  # creating a loop to iterate through the obj1, obj2
    obj.age()

