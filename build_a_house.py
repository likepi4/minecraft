# build a house
from mcpi import minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlocks(pos.x + 0, pos.y + 0, pos.z + 0,
 pos.x + 10, pos.y + 10, pos.z + 10, 17)
mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1,
 pos.x + 9, pos.y + 9, pos.z + 9, 0)

mc.setBlocks(pos.x + 4, pos.y, pos.z,
 pos.x + 6, pos.y + 3, pos.z, 0)