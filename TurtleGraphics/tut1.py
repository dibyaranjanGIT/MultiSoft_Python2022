'''
Documentation : https://docs.python.org/3/library/turtle.html
Turtle module uses tkinter under the hood to create GUI
'''

# Creating our first program
from turtle import Turtle, Screen

bob = Turtle()  # This is the new turtle class object
bob.shape("turtle") # To change the shape of the turtle
bob.color('red') # To change the color of the turtle
bob.forward(100) # To move forward by 100 places
bob.right(90) # To make the turtle turn right

screen = Screen()  # This screen helps us to have the turtle in the window
screen.exitonclick()  # To exit on click
