import turtle
import random

turtle.speed(10)
turtle.penup()
turtle.pensize(1)
turtle.goto(0, -1)
turtle.pendown()
turtle.circle(1)

turtle.penup()
turtle.goto(-1, -1)
turtle.pendown()
turtle.forward(2)
turtle.left(90)
turtle.forward(2)
turtle.left(90)
turtle.forward(2)
turtle.left(90)
turtle.forward(2)
turtle.penup()

numberOfHits = 0
dots = 1000000
import math

for i in range(0, dots + 1): 
    turtle.goto(0, 0)
    y = random.uniform(-1, 1)
    x = random.uniform(-1, 1)
    length = math.sqrt(x**2 + y**2)

    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(1, "black")
    turtle.penup()

    if length <= 1: 
        numberOfHits += 1

pi_estimation = 4 * numberOfHits / dots

print(f'PI is estimated to be {pi_estimation:4f}')







