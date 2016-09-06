#https://compuzzle.wordpress.com/2015/05/04/python-turtle-cheat-sheet-and-geometric-shapes/
import turtle

turtle.hideturtle()                 
turtle.speed('fastest')             
turtle.tracer(False)                

size=1
num_squares = 300

for i in xrange(num_squares): 
  turtle.forward(size)
  turtle.right(91)
  size = size + 1

turtle.tracer(True)
turtle.done()
