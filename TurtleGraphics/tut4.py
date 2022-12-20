## Creating a pop up window using turtle
## The pop up should be set up in the screen not the turtle object
from turtle import Turtle, Screen

bob = Turtle()  # This is the new turtle class object
bob.shape("turtle")

screen = Screen()
screen.setup(width=600, height=500)
user_input = screen.textinput(title="Your input", prompt="Please provide 'Yes' or 'No' ")
print(user_input)
screen.exitonclick()