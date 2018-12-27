#https://docs.python.org/3.2/library/turtle.html
from turtle import *
bart = Turtle()
color("red", "yellow")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
