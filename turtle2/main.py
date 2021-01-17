from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():  # define a function to bind to the onkey() function
    tim.fd(10)


def move_backwards():
    tim.bk(10)


def move_counter_clockwise():
    tim.right(90)


def move_clockwise():
    tim.left(90)


def clear():
    tim.clear()


# grab the screen object and tell it to listen
screen.listen()
# call the bound user-defined function move_forward()
# we don't pass in the parens ()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_clockwise)
screen.onkey(key="d", fun=move_counter_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()