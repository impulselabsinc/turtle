#https://docs.python.org/3.2/library/turtle.html
import turtle
bart = turtle.Turtle()
bart.color("red", "yellow")
bart.begin_fill()
while True:
    bart.forward(200)
    bart.left(170)
    if abs(bart.pos()) < 1:
        break
bart.end_fill()

turtle.done()
