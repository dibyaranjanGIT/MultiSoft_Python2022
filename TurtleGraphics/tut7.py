## X and Y co-ordinates of the turtle moving
from turtle import Turtle, Screen

bob = Turtle()  # This is the new turtle class object
bob.shape("turtle")

screen = Screen()
screen.setup(width=600, height=500)

print(bob.xcor())
print(bob.ycor())

bob.forward(30)

print(bob.xcor())
print(bob.ycor())

screen.exitonclick()