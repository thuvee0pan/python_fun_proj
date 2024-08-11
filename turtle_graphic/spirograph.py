from turtle import Turtle, Screen, colormode
from random import randrange

tim = Turtle()
s = Screen()
colormode(255)
tim.speed(15)

heading = tim.heading()
def random_color():
    R = randrange(0, 257, 10)
    G = randrange(0, 257, 10)
    B = randrange(0, 257, 10)
    return (R, G, B)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.setheading( tim.heading() + size_of_gap)
        tim.circle(100)


draw_spirograph(5)


s.exitonclick()