from turtle import *
from random import randint
bgcolor("yellow")
colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'cyan']
for i in range(200):
    penup()
    r = randint(10,50)
    setx(randint(-200,200))
    sety(randint(-200,200))
    color(colors[randint(0,len(colors)-1)])
    pendown()
    circle(r)

    exitonclick()