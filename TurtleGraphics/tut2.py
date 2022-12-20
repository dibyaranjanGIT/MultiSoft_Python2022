## Pen up and move forward

from turtle import Turtle, Screen

bob = Turtle()  # This is the new turtle class object
bob.shape("turtle")

bob.forward(20)
bob.penup()
bob.forward(20)


screen = Screen()  # This screen helps us to have the turtle in the window
screen.exitonclick()



## How to draw a dashed line
# from turtle import Turtle, Screen
#
# bob = Turtle()
# for _ in range(10):
#     bob.forward(10)
#     bob.penup()
#     bob.forward(10)
#     bob.pendown()
#
# screen = Screen()
# screen.exitonclick()

## How to draw beautiful rectangle shape
# from turtle import Turtle, Screen
# tim = Turtle()
#
# num_sides = 5
#
# for i in range(num_sides):
#     angle = 360 / num_sides
#     tim.forward(100)
#     tim.right(angle)
#
# screen = Screen()
# screen.exitonclick()