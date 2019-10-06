# connect to minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()

# set x, y and z variables to represent coordinates
x = pos.x
y = pos.y
z = pos.z

width = 10
height = 5
length = 6

blockType = 4
air = 0
mc.setBlocks(x, y, z, x + width, y + height,
            z + length, blockType)


