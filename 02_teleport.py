# connect to minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# set x, y and z variables to represent coordinates
x = 10
y = 110
z = 12

# change the player's position
mc.player.setTilePos(x, y, z)