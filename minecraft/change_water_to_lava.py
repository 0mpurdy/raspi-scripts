from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

mc.postToChat('test')
mc.postToChat('Lava is %d' % block.LAVA.id)
mc.postToChat('TNT is %d' % block.TNT.id)
mc.postToChat('Water is %d' % block.WATER.id)

x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, 38)

for i in range(10):
    for j in range(10):
        block_id = mc.getBlock(x-i, y-j, z-1)
        # mc.postToChat('Checking block %d,%d: %d' % (i, j, block_id))
        if (block_id == block.WATER.id):
            mc.setBlock(x-i, y-j, z-1, block.TNT.id)
