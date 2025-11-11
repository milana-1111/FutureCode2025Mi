import turtle
import random

screen = turtle.Screen()
screen.bgcolor("pink")
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(0)
colors = ["yellow", "white", "red", "cyan", "blue", "green"]

for i in range(6):
    for color in colors:
        pen.color(color)
        pen.circle(100)
        pen.penup()
        pen.forward(150)
        pen.pendown()

        for _ in range(3):
            pen.forward(80)
            pen.left(120)
        pen.penup()
        pen.backward(150)
        pen.pendown()
        pen.left(50)

screen.exitonclick()