__author__ = 'chisaton'


import turtle

scr = turtle.Screen()
timmy = turtle.Turtle()

def square(aturtle, side):
    for x in range(4):
        aturtle.forward(side)
        aturtle.left(90)

square(timmy, 120)

scr.mainloop()

