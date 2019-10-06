# connect to minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

blockType = 10
mc.setBlock(x, y, z, blockType)