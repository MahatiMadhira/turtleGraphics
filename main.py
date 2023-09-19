import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

# draw a square
# for i in range(0,4):
#     timmy.forward(100)
#     timmy.right(90)

# draw a dashed line using penup() and pendown()
# for _ in range(50):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# drawing different shapes in different colors
# shape = 3
#
# while shape < 15:
#     angle = 360 / shape
#     timmy.color(random.random(), random.random(), random.random())
#     for _ in range(shape):
#         timmy.forward(50)
#         timmy.right(angle)
#     shape += 1

# RANDOM WALK
timmy.speed("fastest")
# timmy.width(15)
turtle.colormode(255)
# angle = [0, 90, 180, 270]
#
def random_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)

    return (r, g, b)
#
#
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(angle))

# DRAWING A SPIROGRAPH
# timmy.circle(100)
gap = 5
timmy.hideturtle()
for _ in range(int(360/gap)):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + gap)




screen = Screen()
screen.exitonclick()














