from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")

"""
A full turn is 360 degrees. To make each shape,
divide 360 by the number corners in the shape 
and use that as the range.
For example... to make a triangle you will use
3 as the range. then using the .right() method,
Turtle will make 3 right turns to form a triangle.
"""
"""
# Long way
for move in range(3):
    t.forward(200)
    t.color("red")
    t.right(120)
for move in range(4):
    t.forward(200)
    t.color("blue")
    t.right(90)
for move in range(5):
    t.forward(200)
    t.color("green")
    t.right(72)
for move in range(6):
    t.forward(200)
    t.color("black")
    t.right(60)
for move in range(7):
    t.forward(200)
    t.color("purple")
    t.right(51)
"""


# Better
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)


"""
# Making a dotted line

for i in range(5):
    t.forward(100)
    t.penup()
    t.forward(100)
    t.pendown()
    t.right(90)
"""


screen = Screen()
screen.exitonclick()
