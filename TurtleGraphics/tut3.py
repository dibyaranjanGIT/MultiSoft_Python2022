## How to set heading of your turtle and how to increate the speed
'''
‘fastest’ :  0
‘fast’    :  10
‘normal’  :  6
‘slow’    :  3
‘slowest’ :  1
'''

from turtle import Turtle, Screen

bob = Turtle()  # This is the new turtle class object
bob.shape("turtle")
#bob.shape("square")

bob.forward(50)
bob.setheading(90)
bob.forward(50)
bob.setheading(360)
bob.speed('fastest')
bob.forward(200)


screen = Screen()  # This screen helps us to have the turtle in the window
screen.exitonclick()

## Here is a programm to generate the random walk of turtle
# from turtle import *
# import random
#
# tim = Turtle()
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#            "SeaGreen"]
# directions = [0, 90, 180, 360]
#
# # to increse the pensize
# tim.pensize(10)
# # to increase the speeed
# tim.speed('fastest')
#
# for _ in range(100):
#     tim.color(random.choice(colors))
#     tim.forward(10)
#     tim.setheading(random.choice(directions))
