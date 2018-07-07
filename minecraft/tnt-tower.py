from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

mc.postToChat('test')
mc.postToChat('Lava is %d' % block.LAVA.id)
mc.postToChat('TNT is %d' % block.TNT.id)

x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, 38)

for i in range(5):
    mc.setBlock(x+2, y+i, z, block.TNT.id)
