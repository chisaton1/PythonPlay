__author__ = 'chisaton'
import turtle

scr = turtle.Screen()

timmy = turtle.Turtle()


def koch(length, iterations):
    if iterations == 1:
        timmy.forward(length)
        timmy.left(90)
        timmy.forward(length)
        timmy.right(90)
        timmy.forward(length)
        timmy.right(90)
        timmy.forward(length)
        timmy.left(90)
        timmy.forward(length)
    else:
        koch(length / 3, iterations - 1)
        timmy.left(90)
        koch(length / 3, iterations - 1)
        timmy.right(90)
        koch(length / 3, iterations - 1)
        timmy.right(90)
        koch(length / 3, iterations - 1)
        timmy.left(90)
        koch(length / 3, iterations - 1)

timmy.penup()
timmy.goto(-150, -150)
timmy.pendown()
timmy.speed(100)
timmy.hideturtle()


koch(400, 6)

scr.mainloop()
