"""
Abstraction refers to hiding unnecessary details to focus on the whole product instead of parts of the project
separately. It is a mechanism that represents the important features without including implementation details.

Abstract methods are defined in the abstract class. They mostly do not have the body, but it is possible to implement
abstract methods in the abstract class. Any subclass deriving from such an abstract class still needs to provide an
implementation for that abstract method.
"""

## Abstraction can be achieved using the concept of encapsulation

# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def print_area(self):
        pass


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def print_area(self):
        return self.length * self.breadth


rect1 = Rectangle(7, 8)
print(rect1.print_area())
