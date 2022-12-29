## How to write on the screen

# import turtle
# from turtle import Turtle, Screen
#
# bob = Turtle()  # This is the new turtle class object
# bob.shape("turtle")
#
# screen = Screen()
# screen.setup(width=600, height=500)
#
# turtle.write("Hello", align='left', font=('Arial', 20, 'bold'))
#
# screen.exitonclick()


## How to hide turtle

import turtle
from turtle import Turtle, Screen

bob = Turtle()  # This is the new turtle class object
bob.shape("turtle")

screen = Screen()
screen.setup(width=600, height=500)

screen.tracer(0)
bob.penup()
bob.goto(-50, 200)
bob.write("MY GUI", align='left', font=('Arial', 20, 'bold'))
bob.hideturtle()

screen.update()
screen.exitonclick()
