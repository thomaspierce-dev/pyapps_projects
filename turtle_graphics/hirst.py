import colorgram
import turtle as t
import random

colors = colorgram.extract('spots.jpg', 10)

# first_color = colors[0]
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


color_list = [(198, 12, 32), (250, 237, 17), (39, 77, 189), (38, 217, 67), (238, 228, 5), (229, 159, 46), (27, 39, 158)]

# 10 x 10 grid
# size 20 (done)
# 50 paces apart

t.colormode(255)
dot_painting = t.Turtle()
dot_painting.speed('fastest')
dot_painting.penup()
dot_painting.ht()

dot_painting.setheading(225)
dot_painting.fd(300)
dot_painting.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    dot_painting.dot(20, random.choice(color_list))
    dot_painting.fd(50)

    if dot_count % 10 == 0:
        dot_painting.setheading(90)
        dot_painting.fd(50)
        dot_painting.setheading(180)
        dot_painting.fd(500)
        dot_painting.setheading(0)

screen = t.Screen()
screen.exitonclick()

# Review Code