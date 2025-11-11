from turtle import *
penup()
speed(20)
for i in range(-400, 401, 100):
    sety(i)
    for j in range(-400,401, 100):
        setx(j)
        pendown()
        circle(50)
        color("green")
        penup()
exitditonclick()
