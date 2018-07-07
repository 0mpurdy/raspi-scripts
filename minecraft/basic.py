from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

mc.postToChat("Hello world!")

x, y, z = mc.player.getPos()

print("%.2f, %.2f, %.2f" %(x, y, z))

mc.setBlock(x+2, y, z, 1)

mc.player.setPos(x, y + 1, z)

mc.setBlock(x+2, y, z, 0)
