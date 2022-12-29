# How to control the movement of turtle
from turtle import Turtle, Screen

bob = Turtle()  # This is the new turtle class object
bob.shape("turtle")
bob.penup()

screen = Screen()
screen.setup(width=600, height=500)


def up():
    bob.setheading(90)
    bob.forward(10)

def down():
    bob.setheading(270)
    bob.forward(10)

def left():
    bob.setheading(180)
    bob.forward(10)

def right():
    bob.setheading(0)
    bob.forward(10)


# to listen by the turtle
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.exitonclick()
