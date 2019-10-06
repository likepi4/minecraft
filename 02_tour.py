# connect to minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# set x, y and z variables to represent coordinates
x = 0
y = 0
z = 0

# change the player's position
mc.player.setTilePos(x, y, z)

# wait 10 seconds
time.sleep(2)

# set x, y and z again
x = 0
y = 0
z = 50

# change the player's position
mc.player.setTilePos(x, y, z)