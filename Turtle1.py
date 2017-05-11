from turtle import *

color("purple")
speed(5)

n = 4 

right(60/2)

for i in range(n):

    forward(50)
    left(60)
    forward(50)
    left(180-60)
    forward(50)
    left(60)
    forward(50)
    if i < n-1:
        right(60 + 180 - 360/n)
