# http://nghiaho.com/?p=1603
import turtle                       # import the turtle module

# give the turtle superpowers
turtle.hideturtle()                 # make the turtle invisible
turtle.speed('fastest')             # make the turtle go superfast
turtle.tracer(False)                # make the turtle's pen invisible

# function to draw one petal
def petal(radius,steps):            # name and parameters for the function
    turtle.circle(radius,90,steps)  # draw the top of the petal
    turtle.left(90)                 # turn
    turtle.circle(radius,90,steps)  # draw the bottom of the petal

# variables
num_petals = 8                      # the number of petals in the flower
steps = 8                           # the length of each petal
radius = 100                        # the width of each petal

# draw the flower
for i in xrange(num_petals):        # use a for-loop
    turtle.setheading(0)            # the direction the turtle is facing
    turtle.right(360*i/num_petals)  # turn the turtle before placing a leaf
    petal(radius,steps)             # call the petal function

turtle.tracer(True)
turtle.done()
