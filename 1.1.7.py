from math import sqrt
from turtle import*
penup()
speed(0)
n = int(input())
count = 0

for i in range(2, n + 1):
    is_simple = True;

    for divisor in range(2, i):
        if i % divisor == 0:
            is_simple = False;
            break
    if is_simple:
        left(7)
        pendown()
        forward (i)
        setx(0)
        sety(0)
        count += 1
        print(i, end=" ")
print("Кол-во простых чисел в диапозоне от 2 до", n, count)
exit()


