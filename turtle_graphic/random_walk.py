from turtle import Turtle, Screen, colormode
from random import randrange, choice


def random_color():
    R = randrange(0, 257, 10)
    G = randrange(0, 257, 10)
    B = randrange(0, 257, 10)

    rgb = (R, G, B)
    return rgb


tim = Turtle()
s = Screen()

colormode(255)
tim.pensize(15)
tim.speed(15)
tim.position()


directions = [0, 90, 180, 270]

print(s.canvwidth, s.canvheight)

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(choice(directions))



s.exitonclick()