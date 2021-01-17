from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet: ", prompt="Which turtle will win the race? Enter a color: (blue, "
                                                            "green, red, orange, or purple) ")
print(f"You bet on {user_bet}")

colors = ["blue", "green", "red", "orange", "purple"]
names = ["tim", "tom", "ted", "titus", "taz"]
x_axis = -230
y_axis = [-100, -50, 0, 50, 100]
all_turtles = []

# for name, color, y in zip(names, colors, y_axis):
#     name = Turtle(shape="turtle")
#     name.color(color)
#     name.penup()
#     name.goto(x=x_axis, y=y)

for i in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=x_axis, y=y_axis[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You WON! {winning_color} is the winner!")
            else:
                print(f"You LOST! {winning_color} is the winner!")

        rand_distance = random.randint(0, 10)  # randint is inclusive
        turtle.forward(rand_distance)


screen.exitonclick()



