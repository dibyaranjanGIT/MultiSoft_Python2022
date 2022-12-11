'''
Polymorphism in Python is the ability of an object to take many forms. In simple words,
polymorphism allows us to perform the same action in many different ways.

The built-in function len() calculates the length of an object depending upon its type. If an object is a string,
it returns the count of characters, and If an object is a list, it returns the count of items in a list

len("Python") # returns 6 as result
len([1,2,3,4,5,6,7,8,9]) # returns 9 as result

Advantage of method overriding:
It is effective when we want to extend the functionality by altering the inherited method. Or the method inherited from
 the parent class doesn’t fulfill the need of a child class, so we need to re-implement the same method in the child
 class in a different way.
Method overriding is useful when a parent class has multiple child classes, and one of that child class wants to
 redefine the method. The other child classes can use the parent class method. Due to this,
 we don’t need to modification the parent class code
'''

# Example
# print(5 + 6)
# print("DIbya" + "Good")


# class Vehicle:
#     def __init__(self, name, color, price):
#         self.name = name
#         self.color = color
#         self.price = price
#
#     def show(self):
#         print('Details:', self.name, self.color, self.price)
#
#     def max_speed(self):
#         print('Vehicle max speed is 150')
#
#     def change_gear(self):
#         print('Vehicle change 6 gear')


# inherit from vehicle class
# class Car(Vehicle):
#     def max_speed(self):
#         print('Car max speed is 240')
#
#     def change_gear(self):
#         print('Car change 7 gear')

## Car Object
# car = Car('Car Dibya', 'Red', 20000)
# car.show()
## calls methods from Car class
# car.max_speed()
# car.change_gear()


#### Overriding the length function ####

class Shopping:
    def __init__(self, basket, buyer):
        self.basket = list(basket)
        self.buyer = buyer

    def __len__(self):
        print('Redefine length')
        count = len(self.basket)
        # count total items in a different way
        # pair of shoes and shir+pant
        return count**2

shopping = Shopping(['Shoes', 'dress', 'beer'], 'Jeeban')
print(len(shopping))