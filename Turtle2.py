
from turtle import *

shape("turtle")
speed(5)

for n in range(6,2,-1):
    if n % 2 ==1:
        color("purple")
    else:
        color("orange")
  
    for i in range(n):
        forward(100)
        left(360/n)
