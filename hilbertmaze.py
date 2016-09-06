#!/usr/bin/python
"""
Based on Gregor Lingl's Python demos: https://code.google.com/p/python-turtle-demo/
"""
import mcturtle.minecraftturtle as minecraftturtle
import mcturtle.minecraft as minecraft
import mcturtle.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
steve = minecraftturtle.MinecraftTurtle(mc,pos)

steve.penblock(block.WOOL.id, 1)
steve.speed(10)


# example derived from
# Turtle Geometry: The Computer as a Medium for Exploring Mathematics
# by Harold Abelson and Andrea diSessa
# p. 96-98
def hilbert(size, level, parity):
    if level == 0:
        return
    # rotate and draw first subcurve with opposite parity to big curve
    steve.up(parity * 90)
    hilbert(size, level - 1, -parity)
    # interface to and draw second subcurve with same parity as big curve
    steve.forward(size)
    steve.down(parity * 90)
    hilbert(size, level - 1, parity)
    # third subcurve
    steve.forward(size)
    hilbert(size, level - 1, parity)
    # fourth subcurve
    steve.down(parity * 90)
    steve.forward(size)
    hilbert(size, level - 1, -parity)
    # a final turn is needed to make the turtle
    # end up facing outward from the large square
    steve.up(parity * 90)

hilbert(2, 4, 1)
