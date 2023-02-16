'''
Polymorphism in Python is the ability of an object to take many forms. In simple words,
polymorphism allows us to perform the same action in many different ways.

In Python, polymorphism is achieved through the use of inheritance and method overriding.

The built-in function len() calculates the length of an object depending upon its type. If an object is a string,
it returns the count of characters, and If an object is a list, it returns the count of items in a list

len("Python") # returns 6 as result
len([1,2,3,4,5,6,7,8,9]) # returns 9 as result

'''


class Animal:
    def make_sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks.")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows.")



dog = Dog()
cat = Cat()

cat.make_sound()   # Output: The cat meows.
dog.make_sound()   # Output: The dog barks.
