import turtle
turtle.speed(1)

turtle.penup()
turtle.color("black")
turtle.pensize(2)
turtle.goto(0, 0)
turtle.pendown()
turtle.circle(100)

turtle.penup()
turtle.goto(-30, 120)
turtle.pendown()
turtle.dot(25, "black")

turtle.penup()
turtle.goto(30, 120)
turtle.pendown()
turtle.dot(25, "black")

turtle.penup()
turtle.goto(-25, 70)
turtle.pendown()
turtle.goto(25, 70) 
turtle.goto(0, 120)
turtle.goto(-25, 70)

turtle.penup()
turtle.goto(0, 30)
turtle.pendown()
turtle.goto(-60, 55)
turtle.goto(0, 30)
turtle.goto(60, 55)

turtle.hideturtle

