import turtle as t
import random

me = t.Turtle()
t.colormode(255)
me.shape('turtle')
me.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap): # need to convert to int so // or int()
        me.color(random_color())
        me.circle(100)
        me.setheading(me.heading() + size_of_gap)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
