from turtle import *

turtle = Turtle()
#turtle.shape("turtle")
#turtle.color("dark orange")
#turtle.forward(25)

def drawStar(penColor, fillColor):
    global turtle
    turtle.color(penColor, fillColor)
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()

drawStar("royal blue", "yellow")

screen = Screen()
screen.exitonclick()
