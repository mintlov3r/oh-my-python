import turtle
turtle.pensize(2)
turtle.speed(10)
turtle.circle(10)
turtle.circle(40)
turtle.circle(80)
turtle.circle(100)

turtle.color("red","yellow")
turtle.begin_fill()

for _ in range(50):
    turtle.forward(200)
    turtle.left(170)
    turtle.end_fill()

turtle.mainloop()