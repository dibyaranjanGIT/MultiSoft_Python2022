## Understanding the turtle co-ordinates
from turtle import Turtle, Screen

bob = Turtle()  # This is the new turtle class object
bob.shape("turtle")

screen = Screen()
screen.setup(width=500, height=500)

## The screen center is (0, 0)
## If we want to make the turtle move to a certain place we can use goto method
bob.penup()
bob.goto(x=-230, y=0)

screen.exitonclick()

