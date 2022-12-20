## Tracer and Update method

from turtle import Turtle, Screen

bob = Turtle()  # This is the new turtle class object
bob.shape("turtle")

screen = Screen()
screen.setup(width=600, height=600)

for _ in range(20):
    bob.forward(10)
    bob.right(45)


screen.tracer(0)
for _ in range(20):
    bob.forward(20)
    bob.right(45)

screen.update() # update the screen
for _ in range(20):
    bob.forward(30)
    bob.right(45)

screen.exitonclick()