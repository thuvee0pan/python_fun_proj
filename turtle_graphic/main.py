from turtle import Turtle, Screen, colormode
from random import randrange

tim = Turtle()
colormode(255)


def random_color():
    R = randrange(0, 257, 10)
    G = randrange(0, 257, 10)
    B = randrange(0, 257, 10)
    return (R, G, B)


def draw_diagram(shape_side):
    angle = 360 / shape_side
    for _ in range(shape_side):
        tim.forward(100)
        tim.left(angle)


for shape_side in range(3, 11):
    tim.pencolor(random_color())
    draw_diagram(shape_side)


s = Screen()
s.exitonclick()