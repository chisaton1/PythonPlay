__author__ = 'chisaton'

import turtle

scr = turtle.Screen()

timmy = turtle.Turtle()


def A(length, iterations):
    if iterations == 1:
        timmy.forward(length)
    else:
        B(length / 3, iterations - 1)
        timmy.left(60)
        A(length / 3, iterations - 1)
        timmy.left(60)
        B(length / 3, iterations - 1)

def B(length, iterations):
    if iterations == 1:
        timmy.forward(length)
    else:
        A(length / 3, iterations - 1)
        timmy.right(60)
        B(length / 3, iterations - 1)
        timmy.right(60)
        A(length / 3, iterations - 1)


timmy.penup()
timmy.goto(-150, -150)
timmy.pendown()
timmy.speed(100000000)
timmy.hideturtle()


A(3000, 8)

scr.mainloop()
