'''
Documentation : https://docs.python.org/3/library/turtle.html
Turtle module uses tkinter under the hood to create GUI
'''

# Creating our first program and screen properties
from turtle import Turtle, Screen

bob = Turtle()  # This is the new turtle class object
bob.shape("turtle") # To change the shape of the turtle


screen = Screen()  # This screen helps us to have the turtle in the window
screen.setup(width=500, height=500) # This will setup the width and height of the window
screen.title("My GUI") # To setup the title of your window
screen.bgcolor("black") # Changing the background color of Turtle
screen.exitonclick()  # To exit on click
