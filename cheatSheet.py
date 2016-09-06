import mcturtle.minecraftturtle as minecraftturtle
import mcturtle.minecraft as minecraft
import mcturtle.block as block

mc = minecraft.Minecraft.create()               # create a connection to the minecraft world
pos = mc.player.getPos()                        # get the location of your game character
steve = minecraftturtle.MinecraftTurtle(mc,pos) # name your turtle and put it near your game character

steve.penblock(block.WOOL.id, 1)                # tell the turtle what block you want to build with

steve.speed(10)                                 # how fast your turtle will build

steve.forward(10)                               # turtle build 10 bricks forward

teve.backward(5)                                # turtle build 5 bricks backward

steve.right(90)                                 # turtle turn right 90 degrees

steve.left(45)                                  # turtle turn left 45 degrees

steve.up(30)                                    # turtle pitch up 30 degrees

steve.down(10)                                  # turtle pitch down 10 degrees

steve.penup()                                   # turtle stop building

steve.pendown()                                 # turtle start building again

steve.setposition(0,0,0)                        # set the turtle's xyz position
steve.setx(0)                                   # set the turtle's x position
steve.sety(0)                                   # set the turtle's y position
steve.setz(0)                                   # set the turtle's z position

turtlePos = steve.position                      # get the turtle's xyz position
print turtlePos.x                               # get the turtle's x position
print turtlePos.y                               # get the turtle's y position
print turtlePos.z                               # get the turtle's z position

print steve.isdown()                            # find out if the pen is down

steve.setheading(90)                            # set the turtle's heading (angle)

steve.setverticalheading(90)                    # set the turtle's vertical headings (angle)

steve.home()                                    # return the turtle to the position it started in
