from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():  # define a function to bind to the onkey() function
    tim.fd(10)


def backwards():
    tim.bk(10)


def turn_right():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_left():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# grab the screen object and tell it to listen
screen.listen()
# call the bound user-defined function move_forward()
# we don't pass in the parens ()
screen.onkey(forward, "w")
screen.onkey(backwards, "s")
screen.onkey(turn_right, "a")
screen.onkey(turn_left, "d")
screen.onkey(clear, "c")

screen.exitonclick()

