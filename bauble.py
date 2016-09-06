import mcturtle.minecraftturtle as minecraftturtle
import mcturtle.minecraft as minecraft
import mcturtle.block as block


mc = minecraft.Minecraft.create()
pos = mc.player.getPos()
steve = minecraftturtle.MinecraftTurtle(mc,pos)

steve.penblock(block.WOOL.id, 1)
steve.speed(10)

steve.penup()
steve.up(90)
steve.forward(50)
steve.down(90)
steve.pendown()



def circle():
    for i in range(60):
        steve.down(6)
        steve.forward(2)

for i in range(30):
    circle()
    steve.right(6)
    steve.penblock(block.MELON.id, 0)
    circle()
    steve.right(6)
    steve.penblock(block.TNT.id, 0)
