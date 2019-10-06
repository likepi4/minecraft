# connect to minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

pos = mc.player.getPos()

# set x, y and z variables to represent coordinates
x = pos.x
y = pos.y
z = pos.z

x = x + random.randint(-10, 10)
mc.player.setPos(x, y, z)