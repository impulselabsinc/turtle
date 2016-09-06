import mcturtle.minecraftturtle as minecraftturtle
import mcturtle.minecraft as minecraft
import mcturtle.block as block
import math

mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
steve = minecraftturtle.MinecraftTurtle(mc,pos)

steve.penblock(block.WOOL.id, 1)
steve.speed(10)

#Drawing shapes and flowers as specified in
#Think Python: An Introduction to Software Design by Allen B. Downey


def polyline(turtle, n, length, angle):
    """Draw n line segments with the given length and
    angle (in degrees) between them.
    """
    for i in range(n):
        turtle.forward(length)
        turtle.left(angle)


def polygon(n, length):
    angle = 360.0/n
    polyline(turtle, n, length, angle)


def arc(turtle, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before the polyline reduces
    # the error caused by the linear approximation of the arc
    turtle.left(step_angle/2)
    polyline(turtle, n, step_length, step_angle)
    turtle.right(step_angle/2)


def circle(turtle, r):
    arc(turtle, r, 360)


def leaf(turtle, r, angle):
    arc(turtle, r, angle)
    turtle.left(180-angle)
    arc(turtle, r, angle)


def flower(turtle, radius, n):
    r = radius/6 * n
    angle = 360/n
    for i in range(n):
        leaf(turtle, r, angle)
        turtle.left(angle+(180-angle))

flower(steve, 30, 5)
