import turtle as t
import random

directions = [0, 90, 180, 270]
colors = ['red', 'blue', 'black', 'yellow', 'purple', 'brown', 'orange']

me = t.Turtle()
t.colormode(255)
me.shape("turtle")
me.pensize(12)
me.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for walk in range(200):
    me.color(random_color())
    me.forward(40)
    me.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()