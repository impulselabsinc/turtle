import mcturtle.minecraftturtle as minecraftturtle
import mcturtle.minecraft as minecraft
import mcturtle.block as block
import math

mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
steve = minecraftturtle.MinecraftTurtle(mc,pos)

steve.penblock(block.WOOL.id, 1)
steve.speed(10)

def square(self, side):
    self.forward(side)
    self.right(90)
    self.forward(side)
    self.right(90)
    self.forward(side)
    self.right(90)
    self.forward(side)

def box(self,side):
    for i in range(side):
        self.forward(side)
        self.right(90)
        self.forward(side)
        self.right(90)
        self.forward(side)
        self.right(90)
        self.forward(side)
        self.right(90)
        self.up(90)
        self.forward(1)
        self.down(90)


def circle(self):
    for i in range(36):
        self.forward(10)
        self.up(20)

box(steve,5)
