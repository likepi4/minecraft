# connect to minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# set x, y and z variables to represent coordinates
x = 6
y = 5
z = 28

blockType = 103

up = 1
mc.setBlock(x, y, z, blockType)

mc.setBlock(x, y + up, z, blockType)
