from turtle import Turtle, Screen, colormode
from random import choice
import  colorgram

# colors = colorgram.extract('hirst_pic.jpg', 50)
# rgb_color = []
# for col in colors:
#     r = col.rgb.r
#     g = col.rgb.g
#     b = col.rgb.b
#     rgb_color.append((r,g,b))

colors = [(245, 241, 233), (227, 234, 242), (245, 234, 239), (233, 242, 236), (208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59), (172, 204, 182), (108, 46, 38), (158, 204, 215), (76, 69, 37), (9, 87, 109)]

tim = Turtle()
s = Screen()
tim.speed(15)
colormode(255)
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(250)
tim.setheading(0)

dotCount = 100
def change_position():
    tim.backward(500)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)


for i in range(1, dotCount + 1):
    tim.dot(20, choice(colors))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)













s.exitonclick()