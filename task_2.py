import random
from turtle import *


def inflation_change():
    return random.randint(-10, 30)


def bar(height, colour):
    color(colour)
    begin_fill()
    for _ in range(2):
        forward(height)
        right(90)
        forward(5)
        right(90)
    end_fill()


def chart():

    speed("slow")

    left(90)
    inflation_rate = 50
    for _ in range(10):
        inflation_rate += inflation_change()
        bar(inflation_rate, "black")
        pu()
        right(90)
        forward(10)
        left(90)
        pd()
    exitonclick()


chart()
