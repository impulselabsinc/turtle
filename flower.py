import mcturtle.minecraftturtle as minecraftturtle
import mcturtle.minecraft as minecraft
import mcturtle.block as block
import math

mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
T = minecraftturtle.MinecraftTurtle(mc,pos)

T.penblock(block.WOOL.id, 1)
T.speed(10)

#Drawing shapes and flowers as specified in
#Think Python: An Introduction to Software Design by Allen B. Downey


def polyline(T, n, length, angle):
    """Draw n line segments with the given length and
    angle (in degrees) between them.
    """
    for i in range(n):
        T.forward(length)
        T.left(angle)


def polygon(n, length):
    angle = 360.0/n
    polyline(T, n, length, angle)


def arc(T, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before the polyline reduces
    # the error caused by the linear approximation of the arc
    T.left(step_angle/2)
    polyline(T, n, step_length, step_angle)
    T.right(step_angle/2)


def circle(T, r):
    arc(T, r, 360)


def leaf(T, r, angle):
    arc(T, r, angle)
    T.left(180-angle)
    arc(T, r, angle)


def flower(T, radius, n):
    r = radius/6 * n
    angle = 360/n
    for i in range(n):
        leaf(T, r, angle)
        T.left(angle+(180-angle))

flower(T, 30, 5)
